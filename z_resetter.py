import pathlib
import time
import webbrowser
from os import listdir, remove, system
from os.path import abspath, isfile, join, splitext

WORKING_PATH = pathlib.Path(__file__).parent.absolute()

"""
The resetter deletes the created .html mindmap file and the .css file after 15 secs.
Before that it will open the created mindmap in the browser.
Console will be cleared.
"""


def reset():
    dir_files = [file for file in listdir(
        WORKING_PATH) if isfile(join(WORKING_PATH, file))]
    PATH = join("file:///", WORKING_PATH,
                "".join(list(filter(lambda x: splitext(x)[1] == ".html", dir_files))))
    webbrowser.open(PATH)
    time.sleep(15)
    remove(
        "".join(list(filter(lambda x: splitext(x)[1] == ".html", dir_files))))
    remove("add.css")
    try:
        system("cls")
    except:
        exit()
