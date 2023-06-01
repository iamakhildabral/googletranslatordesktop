import tkinter as tk
import ttkbootstrap as ttk
from googletrans import Translator

window = ttk.Window(themename='darkly')
window.title("Google Translator Desktop")
window.geometry('600x500')


def translate_text():
    usertext = user_text.get()
    translator = Translator()
    translation = translator.translate(usertext, dest='hi')
    translated_text_var.set(translation.text)


# creating entrybox  for the user to translate

user_text = ttk.Entry(master=window, textvariable="", font='Calibri 16')
user_text.pack()

translate_button = ttk.Button(master=window, text="Translate", command=translate_text)
translate_button.pack()

translated_text_var = tk.StringVar()
translated_text = ttk.Label(master=window, text="your translated text will come here",textvariable=translated_text_var, font='Calibri 16',)
translated_text.pack()

window.mainloop()
