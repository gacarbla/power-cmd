import json
import os
from configparser import ConfigParser

def fixCHars(text):
    text = text.replace("Ã", "\u00c1").replace("Ã¡", "\u00e1") # á
    text = text.replace("Ã‰", "\u00c9").replace("Ã©", "\u00e9") # é
    text = text.replace("Ã", "\u00cd").replace("Ã­", "\u00ed") # í
    text = text.replace("Ã“", "\u00d3").replace("Ã³", "\u00f3") # ó
    text = text.replace("Ãš", "\u00da").replace("Ãº", "\u00fa") # ú

    text = text.replace("Ãš", "\u00d1").replace("Ã±", "\u00f1") # ñ
    text = text.replace("Â¿", "\u00bf")                         # ¿
    return text

class Translation:

    @staticmethod
    def Get_Language():
        Config_file = "src/config/config.ini"
        Parser = ConfigParser()
        Parser.read(Config_file)
        Lang = Parser["Settings"]["language"]
        filename = "src/lang/{}.json".format(Lang)
        if os.path.isfile(filename):
            filename = filename
        else:
            filename = "src/lang/english.json"
        return filename

    @staticmethod
    def Translate_Language(filename, List, Row):
        reader = open(filename, )
        parser = json.loads(reader.read())
        try:
            if List == "Configuration" or List == "Username" or List == "Website" or List == "Report":
                Phrase = parser[List][0][Row]
            else:
                Phrase = parser[List][Row]
            return fixCHars(Phrase)
        except Exception as e:
            filename = "Lang/english.json"
            reader = open(filename, )
            parser = json.loads(reader.read())
            if List == "Configuration" or List == "Username" or List == "Website" or List == "Report":
                Phrase = parser[List][0][Row]
            else:
                Phrase = parser[List][Row]
            return fixCHars(Phrase)
        
    @staticmethod
    def Check_Language(lang):
        filename = "src/lang/{}.json".format(lang)
        return os.path.isfile(filename)