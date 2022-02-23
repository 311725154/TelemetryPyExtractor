
import tkinter as tk
from tkinter import ttk
import header
import controler


def extract():
    """
    action function for extract button
    :return: void
    """
    header.source_folder_path = folder_path.get()
    # "extract telemetry from mp4"
    print("test: "+header.source_folder_path)


if __name__ == '__main__':

    win = tk.Tk()

    # main window elements
    win.title("Metadata Extractor")
    win.geometry("300x100")

    # local variables
    folder_path = tk.StringVar()

    # folder path label
    ttk.Label(win, text="Source Folder Path:").grid(column=0, row=0, sticky=tk.NW)

    # entry for folder path
    ttk.Entry(win, width=40, textvariable=folder_path).grid(column=0, row=1, sticky=tk.NW)

    # lunch button
    ttk.Button(win, text='Extract', command=extract).grid(column=0, row=2, sticky=tk.NW)

    win.mainloop()
