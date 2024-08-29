import tkinter as tk

def populate_listbox(listbox, items):
    # Clear the current listbox contents
    listbox.delete(0, tk.END)
    
    # Insert each item from the items list into the listbox
    for item in items:
        listbox.insert(tk.END, item)

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack(pady=20)

# List of items to display
items = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape"]

# Call the function to populate the listbox
populate_listbox(listbox, items)

# Start the Tkinter event loop
root.mainloop()




def print_list(listbox):
    listbox.delete(0, tk.END)

    data=db.cursor()
    data.execute("SELECT * FROM enigma")

    for item in data:
        listbox.insert(tk.END, item)

    db.commit()

listbox = tk.Listbox(page2)
listbox.pack(pady=20)
print_list(listbox)