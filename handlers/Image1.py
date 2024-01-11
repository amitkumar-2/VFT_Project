import tkinter as tk
from PIL import Image, ImageTk

def image_handler(frame, image_path, width, height, x, y,command=None, image_path_02 = None, direct_img = None):
    image_base_path = f"C:/Users/cti-2/OneDrive/Documents/Vehicle-Fitness-Test/bhavna_vft/"
    try:            
        if image_path_02 != None:
            img = Image.open(image_base_path + image_path_02)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(frame, image=img_tk, bg='#0E0E0E')
            img_label.image = img_tk
            img_label.place(x=x, y=y)
        else:
            if direct_img != None:
                img = direct_img
            else:
                img = Image.open(image_base_path + image_path)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)
            
            img_label = tk.Label(frame, image=img_tk, bg='#0E0E0E')
            img_label.image = img_tk
            img_label.place(x=x, y=y)

        if command:
            button = tk.Button(frame, image=img_tk, bg="#0E0E0E", command=command,
                                borderwidth=0, relief='flat', activebackground="#0E0E0E", activeforeground='black')
        else:
            button = tk.Label(frame, image=img_tk, bg="#0E0E0E")
        button.image = img_tk
        button.place(x=x, y=y)
    except Exception as e:
        print(f"Error loading ... {image_path}: {e}")






