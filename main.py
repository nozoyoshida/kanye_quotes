from tkinter import *
import requests
from gtts import gTTS
import os
import pygame
from os import path
from pydub import AudioSegment


def get_quote():
    URL = 'https://api.kanye.rest'
    response = requests.get(url=URL)
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)

    kanye_voice = quote
    language = 'en'
    kanye_object = gTTS(text=kanye_voice, lang=language, slow=False)
    kanye_object.save("kanye.mp3")
    AudioSegment.from_mp3("kanye.mp3").export('kanye.ogg', format='ogg')
    pygame.mixer.init()
    pygame.mixer.music.load("kanye.ogg")
    pygame.mixer.music.play(loops=0)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.gif")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
    "Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.gif")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
