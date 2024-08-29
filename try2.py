import tkinter as tk
from tkinter import messagebox

def on_button_click(button_name):
    if button_name == "Button 1":
        messagebox.showinfo("Info", "You clicked Button 1!")
    elif button_name == "Button 2":
        messagebox.showinfo("Info", "You clicked Button 2!")
    elif button_name == "Button 3":
        messagebox.showinfo("Info", "You clicked Button 3!")
    else:
        messagebox.showerror("Error", "Unknown button!")

# Create the main window
root = tk.Tk()
root.title("Button Click Example")

# Create Buttons and link them to the on_button_click function with different arguments
button1 = tk.Button(root, text="Button 1", command=lambda: on_button_click("Button 1"))
button2 = tk.Button(root, text="Button 2", command=lambda: on_button_click("Button 2"))
button3 = tk.Button(root, text="Button 3", command=lambda: on_button_click("Button 3"))

# Pack the buttons into the window
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()