from tkinter import Tk, filedialog

from configurations import Configs, Metrics
from Input import Input
from z_resetter import reset
import time

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename(
        title="Select a list!", filetypes=[("Text files", ".txt")])
    root.destroy()
    start = time.perf_counter()
    Input.take(file_name)
    reset()
    print(time.perf_counter() - start - 15.0)
