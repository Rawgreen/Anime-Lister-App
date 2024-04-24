import tkinter as tk
import customtkinter
import json


class InnerFrames(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class App(customtkinter.CTk):
    def __init__(self, profile_name: str = "Rawwhite"):
        super().__init__()
        self.profile_name = profile_name
        self.__unpack_json()
        self.scrollable_frame = ScrollableFrame(self, width=560, height=660)
        self.scrollable_frame.grid(row=0, column=0, padx=30, pady=25)

    def __unpack_json(self):
        alist_path = "Anime List Data/{name}.json"
        # open given profile name's anime list
        with open(alist_path.format(name=self.profile_name), "r", encoding="utf-8") as file:
            alist = json.load(file)
        # loop through an anime list
        for item in alist:
            # Unpacking json objects into variables
            if isinstance(item, dict):
                (
                    self.status,  # 1-currently watching, 2-completed, 3-on hold, 4-dropped, 5-NULL, 6-Plan to watch
                    self.score,  # given score by the list owner
                    self.num_watched_episodes,
                    self.anime_title,
                    self.anime_title_eng,
                    self.anime_airing_status,  # 2-completed series, 1-currently airing
                    self.anime_id,
                    self.anime_score_val,  # average score given by MAL users
                    self.anime_popularity,  # popularity ranking in anime database
                    self.genres,
                    self.anime_image_path,  # image url
                    self.anime_start_date,
                    self.anime_end_date,
                ) = item.values()


def main():
    app = App(profile_name="Rawwhite")
    app.geometry("640x720")
    app.mainloop()


if __name__ == "__main__":
    main()
