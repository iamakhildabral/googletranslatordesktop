import tkinter as tk
import ttkbootstrap as ttk
from googletrans import Translator

window = ttk.Window(themename='darkly')
window.title("Google Translator Desktop")
window.geometry('800x650')


def translate_text(event=None):
    usertext = user_text.get()
    translator = Translator()
    translation = translator.translate(usertext, dest='hi')
    translated_text_var.set(translation.text)



# creating entrybox  for the user to translate

user_text = ttk.Entry(master=window, textvariable="", font='Calibri 16',width=35)
user_text.pack(pady=50,padx=10)


translate_button = ttk.Button(master=window, text="Translate", command=translate_text)
translate_button.pack(pady=30)

window.bind('<Return>', translate_text)


output_label = ttk.Label(master=window, text="Translated Text",font='Calibri 14')
output_label.pack(pady=20)

# showing the converted value
translated_text_var = tk.StringVar()
translated_text = ttk.Label(master=window,textvariable=translated_text_var, font='Calibri 16',)
translated_text.pack(pady=30)

window.mainloop()
