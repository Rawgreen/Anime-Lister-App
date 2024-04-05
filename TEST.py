import customtkinter
#
#
# class MyFrame(customtkinter.CTkScrollableFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)
#
#         # add widgets onto the frame...
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=0, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=1, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=2, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=3, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=4, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=5, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=6, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=7, column=0, padx=20, pady=30)
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=8, column=0, padx=20, pady=30)
#
#
# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.my_frame = MyFrame(master=self, width=300, height=200)
#         self.my_frame.grid(row=0, column=0, padx=20, pady=20)
#
#
# app = App()
# app.mainloop()


class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=1, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=2, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=3, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=4, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=5, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=6, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=7, column=0, padx=20, pady=30)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=8, column=0, padx=20, pady=30)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self, width=300, height=200, corner_radius=2)
        self.my_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


app = App()
app.mainloop()
