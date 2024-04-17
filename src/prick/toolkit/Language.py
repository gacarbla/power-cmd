import json
import os
from configparser import ConfigParser

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
            return Phrase
        except Exception as e:
            filename = "Lang/english.json"
            reader = open(filename, )
            parser = json.loads(reader.read())
            if List == "Configuration" or List == "Username" or List == "Website" or List == "Report":
                Phrase = parser[List][0][Row]
            else:
                Phrase = parser[List][Row]
            return Phrase
        
    @staticmethod
    def Check_Language(lang):
        filename = "src/lang/{}.json".format(lang)
        return os.path.isfile(filename)