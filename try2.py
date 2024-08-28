import tkinter as tk

def show_items(items):
    # Clear the listbox before adding new items
    listbox.delete(0, tk.END)
    
    # Add each item to the listbox
    for item in items:
        listbox.insert(tk.END, item)

# Create the main window
root = tk.Tk()
root.title("Item List")

# Create a Listbox to show items
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

# Create a sample list of items
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# Call the function to show items immediately
show_items(items)

# Start the main event loop
root.mainloop()