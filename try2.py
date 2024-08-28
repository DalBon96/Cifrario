import tkinter as tk

# Step 1: Create the main application window
root = tk.Tk()
root.title("List of Strings")
root.geometry("300x200")

# Step 2: Create a Listbox widget and populate it with the list of strings
strings_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]
listbox = tk.Listbox(root)

for item in strings_list:
    listbox.insert(tk.END, item)

listbox.pack(fill=tk.BOTH, expand=True)

# Step 3: Run the main event loop
root.mainloop()