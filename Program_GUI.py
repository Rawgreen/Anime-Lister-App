import tkinter as tk
import customtkinter
import json


class AnimeListGuiFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = AnimeListGuiFrame(master=self, width=300, height=200, corner_radius=2)
        self.my_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


def main():
    app = App()
    app.geometry("740x480")
    app.mainloop()


if __name__ == "__main__":
    main()
