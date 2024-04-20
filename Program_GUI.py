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
    def __init__(self):
        super().__init__()


def main():
    # alist_path = "Anime List Data/{name}.json"
    with open("Anime List Data/Rawwhite.json", "r", encoding="utf-8") as file:
        alist = json.load(file)
    # print(alist)
    for item in alist:
        # Unpacking dict into variables
        if isinstance(item, dict):
            (
                status,         # 1-currently watching, 2-completed, 3-on hold, 4-dropped, 5-NaN, 6-Plan to watch
                score,          # given score by the list owner
                num_watched_episodes,
                anime_title,
                anime_title_eng,
                anime_airing_status,    # 2-completed series, 1-currently airing
                anime_id,
                anime_score_val,        # average score given by MAL users
                anime_popularity,       # popularity ranking in anime database
                genres,
                anime_image_path,       # image url
                anime_start_date,
                anime_end_date,
            ) = item.items()
            # print(anime_title_eng)

    app = App()
    app.geometry("640x720")
    app.mainloop()


if __name__ == "__main__":
    main()
