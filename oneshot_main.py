import tkinter as tk
import subprocess
import os
import sys
from tkinter import PhotoImage
from PIL import ImageTk, Image
import pygame
import webbrowser
pygame.mixer.init()

def run_pygame_script_and_exit():
    if sys.platform == "win32":
        subprocess.Popen(['python', 'oneshot.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.Popen(['python3', 'oneshot.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         preexec_fn=os.setpgrp)
    root.quit()
    root.destroy()

def play_music():
    pygame.mixer.music.load("Files/sounds/bg_menu.ogg")
    pygame.mixer.music.play(loops=-1)

root = tk.Tk()
root.title("Oneshot * Main menu")
icon = PhotoImage(file='Files/Sprites and pictures/pictures/icon.png')
root.iconphoto(False, icon)

window_width = 1200
window_height = 700

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

play_music()
root.resizable(False, False)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

bg_image = Image.open("Files/Sprites and pictures/pictures/bg2.png")
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def open_link(event):
    webbrowser.open_new_tab("https://oneshot-journey-of-hope-fsklebp.gamma.site/")
def on_enter(event):
    event.widget.config(fg="yellow")


def on_enter_info(event):
    event.widget.config(fg="blue")

def on_leave(event):
    event.widget.config(fg="white")

start_button = tk.Label(root, text="Start", font=("PixelFont", 48), fg="white", bg="#15011d")
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)
start_button.bind("<Button-1>", lambda event: run_pygame_script_and_exit())
start_button.place(x=window_width//2 + 450, y=window_height - 100)

quit_button = tk.Label(root, text="Quit", font=("PixelFont", 48), fg="white", bg="#1a0025")
quit_button.bind("<Enter>", on_enter)
quit_button.bind("<Leave>", on_leave)
quit_button.bind("<Button-1>", lambda event: root.quit())
quit_button.place(x=window_width//2 , y=window_height - 100)



info_button = tk.Label(root, text="Info", font=("PixelFont", 48), fg="white", bg="#15011d")
info_button.bind("<Enter>", on_enter_info)
info_button.bind("<Leave>", on_leave)
info_button.bind("<Button-1>", open_link)
info_button.place(x=window_width//2 - 600, y=window_height - 100)
root.mainloop()
