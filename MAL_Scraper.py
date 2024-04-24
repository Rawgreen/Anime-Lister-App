import json
import requests
import os
import re
from bs4 import BeautifulSoup


class MALProfile:
    def __init__(self, profile_url: str):
        # Store important variables for later usage.
        self.__class_dict = dict()
        self.url = profile_url
        self.__message = ""

        self.__class_dict.setdefault("Profile URL", self.url)
        self.__class_dict.setdefault("Message", self.__message)
        self._website_response = requests.get(self.url)

        if self._website_response:
            self.__class_dict.setdefault("Status Code", self._website_response.status_code)
            self.soup = BeautifulSoup(self._website_response.text, "html.parser")
        else:
            raise Exception(f"Non-success status code: {self._website_response.status_code}")

    def profile_name(self):
        """Extracts the profile name from the provided URL and stores it in the class dictionary.

        This method attempts to extract the profile name using a regular expression pattern (`([^/]+)$`).
        If the pattern matches the URL, it captures the last part (assumed to be the profile name)
        and stores it in the class dictionary under the key "Profile Name".
        If the pattern fails to match,
        an error message indicating the pattern was not found
        is stored in the dictionary under the key "Message".
        The method then exits.

        **Raises:**

            Exception:
            (Implicitly raised by `exit()` call) An exception exits the program if the pattern is not found.
        """

        regex_pattern = "([^/]+)$"
        profile_name_payload = re.search(regex_pattern, self.url)
        if profile_name_payload:
            result = profile_name_payload.group(1)
            self.__class_dict.setdefault("Profile Name", result)
        else:
            message = "Pattern not found in the URL"
            self.__class_dict.update({"Message": message})
            exit(self.__class_dict.get("Message"))

    def profile_picture(self, soup: BeautifulSoup):
        """Scrapes the user's profile picture from MyAnimeList.net and downloads it.

        This method attempts to find the profile picture using the CSS selector `.lazyload`.
        If the
        image is found, it extracts the image URL from the `data-src` attribute and downloads the
        image binary data using the `requests` library.
        The downloaded image is then saved as a JPG
        file named after the user's profile name in a folder named "images".

        **Raises:**

            Exception: If the profile picture is not found or the `data-src` attribute is missing.
                     The error message is stored in the `_class_dict` attribute under the key "Message".
        """

        profile_picture_payload = soup.find("img", class_="lazyload")
        if profile_picture_payload and "data-src" in profile_picture_payload.attrs:
            image_link = profile_picture_payload["data-src"]
            self.__class_dict.setdefault("Profile Picture Link", image_link)
            image_binary_form = requests.get(image_link)
            download_folder = "Images/Profile Images"
            os.makedirs(download_folder, exist_ok=True)
            file_path = os.path.join(download_folder, f"{self.__class_dict['Profile Name']}.jpg")
            with open(file_path, "wb") as image:
                image.write(image_binary_form.content)
        else:
            message = "Image not found or data-src attribute missing."
            self.__class_dict.update({"Message": message})
            exit(self.__class_dict.get("Message"))

    def anime_list(self, soup: BeautifulSoup):
        """Scrapes the user's anime list from MyAnimeList.net and saves the data to a JSON file.

            This method first tries to find the link to the user's anime list using the CSS selector
            `.btn-profile-submit.fl-l`.
            If the link is found, it extracts data for each anime entry
            including status, score,
            number of watched episodes, title (English and Japanese),
            airing status,
            ID, genres, image path, start and end date strings.
            This data is then saved to a JSON file
            named after the user's profile name in a folder named "list data".

            **Raises:**

                Exception: If the anime list link is not found or the CSS selector is missing.
                The error
                         message is stored in the `_class_dict`
                         attribute under the key "Message".
            """

        anime_list_link = soup.find("a", class_="btn-profile-submit fl-l")
        if anime_list_link and "href" in anime_list_link.attrs:
            list_link = anime_list_link["href"]
            self.__class_dict.setdefault("Anime List", list_link)
            self.scrape_anime_list()
        else:
            message = "Anime list link not found or 'class=btn-profile-submit fl-l' is missing"
            self.__class_dict.update({"Message": message})
            exit(self.__class_dict.get("Message"))

    def scrape_anime_list(self):
        """Scrapes and saves the user's anime list data using the MyAnimeList API.

        This function utilizes the MyAnimeList API to retrieve the user's anime list
        data in a single request with pagination handled through an offset value.
        It iterates through the entries in the retrieved data and extracts information
        for each anime entry using a predefined list of important tags.
        The extracted data is then saved to a JSON file.

        **Attributes:**

            important_tags (list):
                A list of strings representing the keys to extract from each anime entry.
            export_folder (str):
                The name of the folder where the JSON file will be saved.
                Defaults to "Anime List Data".
            file_path (str):
                The path to the JSON file where the scraped data is saved.
            session (requests.Session):
                A session object used for making API requests.
            list_api (str):
                The base URL for the API endpoint that provides the anime list data.
            json_offset (int):
                An offset value used for pagination within the API call.
    """

        important_tags = ["status", "score", "num_watched_episodes",
                          "anime_title", "anime_title_eng", "anime_airing_status",
                          "anime_id", "anime_score_val", "anime_popularity",
                          "genres", "anime_image_path", "anime_start_date_string",
                          "anime_end_date_string",
                          ]
        export_folder = "Anime List Data"
        os.makedirs(export_folder, exist_ok=True)
        file_path = os.path.join(export_folder, f"{self.__class_dict['Profile Name']}.json")
        session = requests.Session()
        json_offset = 0
        list_api = "https://myanimelist.net/animelist/{name}/load.json?offset={json_offset}"

        max_retries = 3  # Define the maximum number of retries for API requests
        retries = 0
        data = []

        with open(file_path, "w", encoding="utf-8") as json_file:
            while True:
                try:
                    response = session.get(list_api.format(name=self.__class_dict.get("Profile Name"),
                                                           json_offset=json_offset))
                    response.raise_for_status()  # Raise an exception for non-200 status codes
                    json_data = response.json()
                    if not json_data:
                        break
                    else:
                        for item in json_data:
                            extracted_data = {key: item[key] for key in important_tags if key in item}
                            data.append(extracted_data)

                except requests.exceptions.RequestException as e:
                    # Handle request exceptions (e.g., connection errors, timeouts)
                    print(f"Error encountered while fetching data: {e}")
                    if retries < max_retries:
                        retries += 1
                        print(f"Retrying request (attempt {retries}/{max_retries})...")
                        continue  # Retry the request
                    else:
                        print(f"Maximum retries reached. Stopping scraping.")
                        break  # Exit the loop after max retries
                finally:
                    # Optional: Close session resources after successful completion or exception
                    session.close()

                json_offset += 300
            if data:
                json.dump(data, json_file, indent=4)

    def scraper(self):
        """ Scrapes profile information from a MyAnimeList.net user profile URL.

        This method fetches the content of the provided URL using the `requests` library.
        If the request is successful (status code 200), it parses the HTML content using BeautifulSoup.

        The method then calls three helper functions to extract specific information:

        * `Profile_name()`: Extracts the profile name from the URL using a regular expression.
        * `Profile_picture()`: Scrapes the user's profile picture URL and downloads the image.
        * `Anime_list()`: Scrapes the user's anime list data and saves it to a JSON file.

        The extracted information is stored in the class dictionary (`_class_dict`).

        **Raises:**

            Exception: If the website returns a non-success status code.
                       The specific status code is included in the exception message.
        """

        self.profile_name()
        self.profile_picture(self.soup)
        self.anime_list(self.soup)

    def get_class_dict(self) -> dict:
        return self.__class_dict


if __name__ == "__main__":
    # Randomly sampled profiles
    link = "https://myanimelist.net/profile/Rawwhite"
    # link = "https://myanimelist.net/profile/deatacitta"
    # link = "https://myanimelist.net/profile/Paulternative"
    test = MALProfile(link)
    test.scraper()
    class_variables = test.get_class_dict()
    for key, value in class_variables.items():
        print(f"{key}: {value}")
