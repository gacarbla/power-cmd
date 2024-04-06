import random as rnd
from tkinter import messagebox as msgb
import os

from src.power import Menu
from src.prick.toolkit import Language, Clear

filename = Language.Translation.Get_Language()
filename

MainMenu = Menu()
Clear.Auto()