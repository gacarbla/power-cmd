from .toolkit import Language, Font

trans = Language.Translation.Translate_Language
tcolor = Font.Color.Text
bcolor = Font.Color.Back
filename = Language.Translation.Get_Language()
filename
error404header = f"!:{tcolor.RED}\n\n{" "*5}{bcolor.RED}{tcolor.BLACK}{" "*15}4 0 4{" "*15}{bcolor.RESET}{tcolor.RESET}\n\n{" "*10}{trans(filename, "Menu", "error404message")}\n\n\n{tcolor.RESET}"
defaulttablehead = f"!:{bcolor.WHITE}{tcolor.BLACK}\n {trans(filename, "Menu", "headerdefault")}{" "*(43-len(trans(filename, "Menu", "headerdefault")))}\n{bcolor.RESET}{tcolor.RESET}"
errortablehead = f"!:{bcolor.WHITE}{tcolor.BLACK}\n {trans(filename, "Menu", "errordefault")}{" "*(43-len(trans(filename, "Menu", "errordefault")))}\n{bcolor.RESET}{tcolor.RESET}"

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
        History = "?page:dg_history"
        Configuration = "?config:dg_config"
        Help = "?help:dg_help"
    class Filemanager:
        Tablehead = defaulttablehead
        Return = "?return"
        By_Extension = "?page:fm_extension"
        By_Letter = "?page:fm_letter"
        By_Word = "?page:fm_word"
        By_Size = "?page:fm_size"
        Help = "?help:fm_help"
    class Tools:
        Tablehead = defaulttablehead
        Return = "?return"
        Key_logger = "?page:tl_keylogger"
        USB_file_copy = "?page:tl_usbcopy"
        Encrypter = "?page:tl_encrypter"
        Help = "?help:tl_help"
    home = "Home"
    notfound = "E404"