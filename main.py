import os.path
import tkinter as tk
from tkinter import messagebox as tkmsg
from tkinter import ttk
import header
import controler


def extract():
    """
    action function for extract button
    :return: void
    """

    # "extract telemetry from mp4"
    try:
        header.source_folder_path = os.path.isdir(folder_path.get())
    except NotADirectoryError:
        tkmsg.showerror("Source Error", "There is no Folder or path: {} \nplease insert correct oath and try again!".format(folder_path.get()))
    except OSError:
        tkmsg.showerror("Permissions Error", "You have no permission to read or write to this destination.\nPlease try other path or contact system administrator.")

    if header.source_folder_path:
        controler.Controller


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
