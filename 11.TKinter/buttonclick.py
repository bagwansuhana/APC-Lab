import tkinter as tk

def show_message():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

label = tk.Label(root, text="Welcome")
label.pack(pady=10)

button = tk.Button(root, text="Click Me",
                   command=show_message)
button.pack()

root.mainloop()