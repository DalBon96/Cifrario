import tkinter as tk
import mysql.connector
from mysql.connector import Error

def populate_listbox(listbox, items):
    # Clear the current listbox contents
    listbox.delete(0, tk.END)
    
    # Insert each item from the items list into the listbox
    for item in items:
        listbox.insert(tk.END, item)

def update_listbox():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT item_column FROM your_table_name")
            rows = cursor.fetchall()
            
            # Extract items from the rows and update the listbox
            items = [row[0] for row in rows]
            populate_listbox(listbox, items)
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create the main window
root = tk.Tk()
root.title("Listbox Update with MySQL")

# Create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack(pady=20)

# Initial empty population
populate_listbox(listbox, [])

# Create a Button to update the listbox from the database
update_button = tk.Button(root, text="Update Listbox from DB", command=update_listbox)
update_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()