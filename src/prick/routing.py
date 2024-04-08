from .toolkit import Language, Font

trans = Language.Translation.Translate_Language
tcolor = Font.Color.Text
bcolor = Font.Color.Back
filename = Language.Translation.Get_Language()
filename
error404header = f"!:{tcolor.RED}\n\n{" "*5}{bcolor.RED}{tcolor.BLACK}{" "*15}4 0 4{" "*15}{bcolor.RESET}{tcolor.RESET}\n\n{" "*10}{trans(filename, "Menu", "error404message")}\n\n\n{tcolor.RESET}"
defaulttablehead = f"!:{bcolor.WHITE}{tcolor.BLACK}\n {trans(filename, "Menu", "headerdefault")}{" "*18}\n{bcolor.RESET}{tcolor.RESET}"
errortablehead = f"!:{bcolor.WHITE}{tcolor.BLACK}\n {trans(filename, "Menu", "errordefault")}{" "*18}\n{bcolor.RESET}{tcolor.RESET}"

class Structure:
    class Home:
        Tablehead = defaulttablehead
        Exit = "?return"
        DeviceDiagnosis = "?menu:Diagnosis"
        FileManager = "?menu:Filemanager"
        Tools = "?menu:Tools"
        Configuration = "?config:config"
    class E404:
        header = error404header
        Tablehead = errortablehead
        Exit = "?return"
        Home = "?menu:Home"
    class Diagnosis:
        Tablehead = defaulttablehead
        Return = "?return"
        Get_Data = "?page:dg_data"
        Help = "?help:dg_help"
    class Filemanager:
        Tablehead = defaulttablehead
        Return = "?return"
        By_FirstLetter = "?page:fm_letter"
        By_FirstWord = "?page:fm_word"
        By_FirstExtension = "?page:fm_extension"
        Help = "?help:fm_help"
    class Tools:
        Tablehead = defaulttablehead
        Return = "?return"
        Key_logger = "?page:tl_keylogger"
        Help = "?help:tl_help"
    home = "Home"
    notfound = "E404"