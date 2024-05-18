import MAL_Scraper as scraper
import Program_GUI as gui


def main():
    # link = "https://myanimelist.net/profile/Rawwhite"
    link = "https://myanimelist.net/profile/deatacitta"
    # link = "https://myanimelist.net/profile/Paulternative"
    test = scraper.MALProfile(link)
    test.scraper()
    gui.start_gui(profile_name="deatacitta")
    # class_variables = test.get_class_dict()
    # for key, value in class_variables.items():
    #     print(f"{key}: {value}")


if __name__ == "__main__":
    main()
