import re
import customtkinter
import json
from PIL import Image, ImageTk


class InnerFrames(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    """
    A custom scrollable frame widget for displaying items.
    """

    def __init__(self, profile_name: str, master, **kwargs):
        """
        Initialize the ScrollableFrame.

        :param master: The parent widget.
        :param kwargs: Additional keyword arguments passed to the super().__init__() method.
        """
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(1, weight=1)
        self.label_list = []
        self.profile_name = profile_name

    def add_item(self, item):
        """
        Add an item to the scrollable frame.

        :param item: The item to add.
        """
        # master is scrollable frame itself
        left_image_frame = InnerFrames(self)
        right_detail_frame = InnerFrames(self)
        left_image_frame.grid(row=len(self.label_list), column=0, sticky="nsw", padx=10, pady=10)
        right_detail_frame.grid(row=len(self.label_list), column=1, sticky="nse", padx=10, pady=10)

        # Load image
        image = Image.open(f"Images/Anime Images/{re.sub(r'[^\w\s]', '', item)}.jpg")
        photo = ImageTk.PhotoImage(image)

        # Create image label in the left frame
        image_label = customtkinter.CTkLabel(master=left_image_frame, text="", image=photo)
        image_label.image = photo
        image_label.grid()

        # Create details label in the right frame
        details_label = customtkinter.CTkLabel(master=right_detail_frame, text=item)
        details_label.grid()
        self.label_list.append(details_label)


class App(customtkinter.CTk):
    """
    Main application class for the Anime Lister Project.

    :param profile_name: The name of the anime list profile to load. Defaults to "Rawwhite".
    """

    def __init__(self, profile_name: str):
        """
        Initialize the App.

        :param profile_name: The name of the anime list profile to load. Defaults to "Rawwhite".
        """
        super().__init__()
        self.geometry("640x720")
        self.title("Anime Lister Project TEST")
        self.profile_name = profile_name
        self.json_items_list = self.__unpack_json()
        self.scrollable_frame = ScrollableFrame(master=self, width=560, height=660, profile_name=profile_name)
        for i in range(len(self.json_items_list)):
            # key, value pair of anime_title attribute of iwoth list item.
            self.scrollable_frame.add_item(self.json_items_list[i][3][1])
        self.scrollable_frame.grid(row=0, column=0, padx=30, pady=25)

    def __unpack_json(self) -> list:
        """
        Unpack JSON data from the selected profile's anime list.

        :return: A list of unpacked JSON items.
        """
        selected_profile = "Anime List Data/{name}.json"
        items_list = []
        with open(selected_profile.format(name=self.profile_name), "r", encoding="utf-8") as file:
            alist = json.load(file)
        for item in alist:
            if isinstance(item, dict):
                json_items = tuple(item.items())
                items_list.append(json_items)
        return items_list


def start_gui(profile_name: str):
    app = App(profile_name=profile_name)
    customtkinter.set_appearance_mode("dark")
    app.mainloop()


if __name__ == "__main__":
    start_gui(profile_name="Rawwhite")
