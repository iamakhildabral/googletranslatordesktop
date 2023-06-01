import tkinter as tk
import ttkbootstrap as ttk
from googletrans import Translator

window = ttk.Window(themename='darkly')
window.title("Google Translator Desktop")
window.geometry('800x650')

# to maximize the window
window.state('zoomed')


def translate_text(event=None):
    usertext = user_text.get("1.0", tk.END)  # Get the content of the Text widget till end
    translator = Translator()
    translation = translator.translate(usertext, dest='hi')
    ##translated_text_var.set(translation.text)
    scrolled_output_text.delete(1.0, tk.END)
    scrolled_output_text.insert(tk.END, translation.text)


# creating text box  for the user to translate

user_text = ttk.Text(master=window, font='Calibri 16', height=8, width=70, wrap=ttk.WORD)
user_text.pack(pady=50, padx=10)

translate_button = ttk.Button(master=window, text="Translate", command=translate_text)
translate_button.pack(pady=30)

window.bind('<Return>', translate_text)


scrolled_output_text = ttk.ScrolledText(master=window,font="Calibri 14")
scrolled_output_text.pack(expand=True,pady=60)



window.mainloop()
