import os
import tkinter as tk
from tkinter import filedialog, ttk, StringVar
from PIL import Image

# Se abre una imagen
def open_image():
    pictures_directory = os.path.expanduser("~").replace("\\", "/") + "/Imágenes"
    filetypes = [
        ('JPEG Image', '*.jpg;*.jpeg'),
        ('PNG Image', '*.png'),
        ('Icon', '*.ico'),
        ('All files', '*.*')
    ]
    filename = filedialog.askopenfilename(initialdir=pictures_directory, filetypes=filetypes)
    
    if filename:
        tk_filename.set(filename)
        ttk.Label(frame, textvariable=tk_filename, font=("Times", 10)).grid(column=0, row=2)
        ttk.Button(frame, text="Go", command=change_image_extension).grid(column=2, row=2)
        ttk.Combobox(frame, textvariable=new_extension, state="readonly", values=(".png", ".jpg", ".ico")).grid(column=1, row=2)
        status_bar.config(text="File selected successfully")
    else:
        status_bar.config(text="No file selected")


# Se crea una nueva imagen con distinta extension
def change_image_extension():
    try:
        filename = os.path.splitext(tk_filename.get())[0]
        image = Image.open(tk_filename.get())
        image.save(filename + new_extension.get())
        status_bar.config(text="File saved successfully")
    except:
        status_bar.config(text="Failed to save file")

# Ventana principal
root = tk.Tk()
root.title("MakiFile")

# Variables
tk_filename = StringVar()
new_extension = StringVar()

# Frame
frame = ttk.Frame(root, padding="20 20 20 20")
frame.grid(column=0, row=0, sticky="nsew")
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Widgets
ttk.Label(frame, text="File Converter", font=("Times", 24)).grid(column=0, row=0, columnspan=3, sticky="nsew")
ttk.Button(frame, text="Choose File", command=open_image).grid(column=0, row=1, sticky="nsew")

status_bar = tk.Label(root, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.grid(column=0, row=1, sticky="ew")


root.mainloop()
