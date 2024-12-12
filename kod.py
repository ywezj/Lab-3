import tkinter as tk
import random
import pygame
from PIL import Image
from itertools import count

def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = window.after(100, lambda :animation(count))

def play_music():
    pygame.mixer.music.load("cs2_maintheme.mp3") 
    pygame.mixer.music.play()

def generator():
    input = key_input.get()
    key = ""
#первый элемент
    for i in range(3):
        key += random.choice(input)
    key += " "
#второй элемент
    for i in range(6):
        if ord(input[i]) - 64 < 10:
            key += str(ord(input[i]) - 64)
        else:
            key += str(ord(input[i]) - 64)[1:]
    key += " "   
#третий элемент 
    for i in range(3):
        key += random.choice(input)

    key_output.delete("0", tk.END)
    key_output.insert(0, key)

if __name__ == "__main__":
    window = tk.Tk()
    window.title('Key generator for Counter Strike 2')
    window.geometry('1500x732')
    pygame.init()

    bg_img = tk.PhotoImage(file='www.png')
    lbl_bg = tk.Label(window, image=bg_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    play_music()

    info = Image.open("result_shoot (1).gif")
    frames = info.n_frames  
    im = [tk.PhotoImage(file="result_shoot (1).gif",format=f"gif -index {i}") for i in range(frames)]
    count = 0
    anim = None
    gif_label = tk.Label(window, image="")
    gif_label.place(relx=0.8, rely=0.79)
    animation(count)

    input_label = tk.Label(window, text='Enter 6 letters in caps: ', font=14)
    input_label.place(relx=0.09, rely=0.09)
    key_input = tk.Entry(window, width=12, font=30)
    key_input.insert(0, 'ABCDEF')
    key_input.place(relx=0.234, rely=0.091)
    
    btn_guess = tk.Button(window, text='Generate KEY', font=14, width=12, command=generator)
    btn_guess.place(relx=0.1, rely=0.18)
    
    output_label = tk.Label(window, text='Game key: ', font=14)
    output_label.place(relx=0.3, rely=0.8)
    key_output = tk.Entry(window, width=30, font=16)
    key_output.place(relx=0.376, rely=0.8)

    window.mainloop()