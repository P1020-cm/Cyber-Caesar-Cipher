import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')

            if mode == "encrypt":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result += new_char
        else:
            result += char

    return result


def process(mode):
    try:
        text = input_box.get("1.0", tk.END).strip()
        shift = shift_slider.get()
        if not text:
            messagebox.showwarning("Warning", "Enter some text!")
            return
        output = caesar_cipher(text, shift, mode)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)
    except:
        messagebox.showerror("Error", "Something went wrong")


def copy_result():
    root.clipboard_clear()
    root.clipboard_append(output_box.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Result copied to clipboard!")


def clear_all():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# ========== GUI Setup ==========

root = tk.Tk()
root.title("Secure Caesar Cipher Tool")
root.geometry("600x450")
root.configure(bg="#0f172a")

title = tk.Label(
    root,
    text="Secure Caesar Cipher Tool",
    font=("Segoe UI", 18, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e293b", bd=2, relief="ridge")
frame.pack(padx=15, pady=10, fill="both", expand=True)

tk.Label(frame, text="Input Text", fg="white", bg="#1e293b").pack(pady=5)
input_box = tk.Text(frame, height=5, bg="#020617", fg="#e5e7eb", insertbackground="white")
input_box.pack(fill="x", padx=10)

tk.Label(frame, text="Shift Value", fg="white", bg="#1e293b").pack(pady=5)
shift_slider = tk.Scale(frame, from_=1, to=25, orient="horizontal", bg="#1e293b", fg="white", troughcolor="#020617")
shift_slider.set(3)
shift_slider.pack(fill="x", padx=20)

btn_frame = tk.Frame(frame, bg="#1e293b")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encrypt", width=12, bg="#38bdf8", command=lambda: process("encrypt")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Decrypt", width=12, bg="#22c55e", command=lambda: process("decrypt")).grid(row=0, column=1, padx=10)

tk.Label(frame, text="Output Text", fg="white", bg="#1e293b").pack(pady=5)
output_box = tk.Text(frame, height=5, bg="#020617", fg="#38bdf8")
output_box.pack(fill="x", padx=10)

extra_frame = tk.Frame(frame, bg="#1e293b")
extra_frame.pack(pady=10)

tk.Button(extra_frame, text="Copy Result", bg="#a78bfa", command=copy_result).grid(row=0, column=0, padx=10)
tk.Button(extra_frame, text="Clear", bg="#f87171", command=clear_all).grid(row=0, column=1, padx=10)

root.mainloop()
