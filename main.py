import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk
from googletrans import Translator

window = ttk.Window(themename='darkly')
window.title("Google Translator Desktop")
window.geometry('800x650')
# to maximize the window
window.state('zoomed')


def translate_text(event=None):
    translate_button.config(state=tk.DISABLED)
    user_entered_text = user_text.get("1.0", tk.END)  # Get the content of the Text widget till end
    try:
        translator = Translator()
        translation = translator.translate(user_entered_text, dest='hi')

        # Update the scrolled text widget with the translated text
        scrolled_output_text.delete(1.0, tk.END)
        scrolled_output_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Error", "Translation failed. Please check your internet connection.")


    # Enable the Translate button after translation is completed
    translate_button.config(state=tk.NORMAL)

# creating text box  for the user to translate

user_text = ttk.Text(master=window, font='Calibri 16', height=8, width=70, wrap=ttk.WORD)
user_text.pack(pady=50, padx=10)

translate_button = ttk.Button(master=window, text="Translate", command=translate_text)
translate_button.pack(pady=30)

window.bind('<Return>', translate_text)

# creating scrolled text for the translated output
scrolled_output_text = ttk.ScrolledText(master=window, font="Calibri 14")
scrolled_output_text.pack(expand=True, pady=60)

# Set the scrollbar colors to match the 'darkly' theme
style = ttk.Style()
style.theme_use("darkly")
style.configure("Vertical.TScrollbar", troughcolor=style.lookup("TFrame", "background"),
                background=style.lookup("TFrame", "background"), darkcolor=style.lookup("TFrame", "background"),
                lightcolor=style.lookup("TFrame", "background"))

# Apply the style to the scrolled text widget
scrolled_output_text.config(yscrollcommand=style.configure("Vertical.TScrollbar"))

window.mainloop()
