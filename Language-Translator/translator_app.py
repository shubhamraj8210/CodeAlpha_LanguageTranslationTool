import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3
import pyperclip

languages = GoogleTranslator(source='auto', target='english').get_supported_languages(as_dict=True)
lang_names = sorted(languages.keys())

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return
    try:
        src = "auto" if src_lang.get() == "auto" else languages[src_lang.get()]
        tgt = languages[tgt_lang.get()]
        translated = GoogleTranslator(source=src, target=tgt).translate(text)
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

root = tk.Tk()
root.title(" Language Translation Tool")
root.geometry("600x550")
root.configure(bg="#f0f4f8")

tk.Label(root, text="Language Translator", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333").pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="From:", bg="#f0f4f8").grid(row=0, column=0, padx=5)
src_lang = ttk.Combobox(frame, values=["auto"] + lang_names, width=20)
src_lang.set("auto")
src_lang.grid(row=0, column=1, padx=5)

tk.Label(frame, text="To:", bg="#f0f4f8").grid(row=0, column=2, padx=5)
tgt_lang = ttk.Combobox(frame, values=lang_names, width=20)
tgt_lang.set("hindi")
tgt_lang.grid(row=0, column=3, padx=5)

tk.Label(root, text="Enter Text:", bg="#f0f4f8", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
input_text = tk.Text(root, height=6, width=65, font=("Arial", 11))
input_text.pack(padx=20, pady=5)

tk.Button(root, text=" Translate", command=translate_text, bg="#4CAF50", fg="white",
          font=("Arial", 12, "bold"), padx=20, pady=5).pack(pady=10)

tk.Label(root, text="Translated Text:", bg="#f0f4f8", font=("Arial", 11, "bold")).pack(anchor="w", padx=20)
output_text = tk.Text(root, height=6, width=65, font=("Arial", 11), state="disabled")
output_text.pack(padx=20, pady=5)

btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text=" Copy", command=copy_text, bg="#2196F3", fg="white", padx=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text=" Speak", command=speak_text, bg="#FF9800", fg="white", padx=15).grid(row=0, column=1, padx=10)

root.mainloop()