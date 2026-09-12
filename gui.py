import tkinter
from collections import deque
from filters import *

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox

dont_quit = True

class SaveState:
    def __init__(self, tk_root=None):
        self.__img_current = None
        self.__img_og = None
        self.__img_backups = deque([])
        self.img_filetypes = IMAGE_FILE_TYPES = [('All files', '.*'),
                    ('BMP', '.bmp'),
                    ('GIF', '.gif'),
                    ('PNG', '.png'),
                    ('TIFF', '.tif'),
                    ('TIFF', '.tiff'),
                    ('JPEG', '.jpg'),
                    ('JPEG', '.jpeg')]

        if tk_root is None:
            self.tk_root = tk.Tk()
        else:
            self.tk_root = tk_root

    def get_current_img(self):
        return self.__image_current

    def set_current_img(self, img):
        if self.__img_current is not None:
            self.__img_backups.appendleft(self.__img_current)
        else:
            self.__img_og = img

            tk_og_img = ImageTk.PhotoImage(img)
            og_img_display = tk.Label(original_frame, image=tk_og_img, bg="white")
            og_img_display.pack()
            #og_img_display.image = tk_og_img

        self.__img_current = img

    def is_img_loaded(self):
        if self.__img_current is not None:
            return True
        else:
            return False

    def load_img(self, str=None):
        if str is None:
            str = tk.filedialog.askopenfilename(filetypes=self.img_filetypes)

        img = Image.open(str)
        tk_og_img = ImageTk.PhotoImage(img)
        if self.__img_current is not None:
            self.__img_backups.appendleft(self.__img_current)
        else:
            self.__img_og = img

            og_img_display = tk.Label(original_frame, image=tk_og_img, bg="white")
            og_img_display.pack()
            og_img_display.image = tk_og_img


# Tkinter Setup
root = tk.Tk()
root.title("Img??")
root.geometry('1024x576+25+25')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)


# Setup save state
save_state = SaveState(root)

# Sidebar setup
sidebar_frame = tk.Frame(root, width=300, bg="indigo")
#sidebar_frame.pack( side=tk.LEFT, fill=tk.Y)
sidebar_frame.grid(column=0, row=0, columnspan=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)

sidebar_frame.grid_rowconfigure(0, weight=1)
sidebar_frame.grid_rowconfigure(0, weight=2)
sidebar_frame.columnconfigure(0, minsize=200)

side_toolbar = tk.Frame(sidebar_frame, width=300, bg="slategrey")
side_toolbar.grid(row=1, padx=5, pady=5, ipadx=5, ipady=5, sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)

# Display img
image_frame = tk.Frame(root, width=500, height=500, bg="grey")
#image_frame.pack(padx=5, pady=5, side=tk.RIGHT, fill=tk.BOTH)
image_frame.grid(column=1, row=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)

tk.Label(image_frame, text="Edited Image", bg="grey", fg="white",).pack(padx=5, pady=5, fill=tk.X)

#OG Img
original_frame = tk.Frame(sidebar_frame, width=300, bg="darkslateblue")
#original_frame.pack(padx=5, pady=5, side=tk.RIGHT, fill=tk.BOTH)
original_frame.grid(row=0, padx=5, pady=5, ipadx=5, ipady=5, sticky=tkinter.W+tkinter.E+tkinter.N+tkinter.S)

og_img_label = tk.Label(original_frame, text="Original Image", bg="grey", fg="white",)
og_img_label.pack(padx=5, pady=5, fill=tk.X)

# Exit button setup
def handle_exit():
    msg_response = messagebox.askyesno(title="Confirm?", message="Confirm quitout?")
    if msg_response is True:
        root.quit()

exit_button = ttk.Button(side_toolbar, text="Exit Program", command=handle_exit)
exit_button.pack(ipadx=5, ipady=5, padx=5, pady=5, expand=True)

# Load img setup
def load_img():
    save_state.load_img()

load_img_button = ttk.Button(side_toolbar, text="Load Img", command=load_img)
load_img_button.pack(ipadx=5, ipady=5, padx=5, pady=5, expand=True)

# Run loop
root.mainloop()