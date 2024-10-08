import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector #MYSQL
from mysql.connector import Error

#CONNECTION
db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="enigma")

# function to get text from entry widget
def print_entry_text():
    entry_text = entry.get()
    entry_key = key.get()
    while True:
            try:
            # Convert the input to an integer
                int(entry_key)
                break  # Exit the loop if conversion is successful
            except Exception as e:
        # Handle the error and display a message box
                messagebox.showerror("Error", f"Invalid Input: {e}")
                entry_key.delete(0, tk.END)
    
    text2 = list(entry_text) #I create the Array
    #new_key=int(key) # i transform the string to int
    ascii_numbers = [ord(char)+int(entry_key) for char in text2] #i transform the values in the list in ASCII and i sum the KEY
        #i transform from ASCII to list of letters
        #and create the edit string
    new_list=[]
    for value in ascii_numbers:
        new_list.append(chr(value))
    label.config(text=''.join(new_list))

    #I save the value to bring in another method
    save_value = ''.join(new_list)
    save_data(entry_text,save_value,entry_key)

#Method to save the text and the EDIT test  FROM print_entry_text()
def save_data(text,text2,key):
    data=db.cursor()
    data.execute("INSERT INTO enigma (message,new_message,number) VALUES (%s,%s,%s)",(text,text2,key))
    db.commit()


##########################################################################################################
##########################################################################################################
#SECOND OPTION OF THE MENU
#SHOW THE LIST
def print_list(listbox,items):
    listbox.delete(0, tk.END)

    for item in items:
        listbox.insert(tk.END, item)


def update_listbox():
    try:
        # Establish a database connection
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="enigma")
        
        if db.is_connected():
            cursor = db.cursor()
            cursor.execute("SELECT * FROM enigma")
            rows = cursor.fetchall()
            
            # Format the rows into a list of strings to display in the Listbox
            items = []
            for row in rows:
                # Assuming the table has columns: id, name, price
                formatted_item = f"ID: {row[0]} | {row[1]} | {row[3]} | {row[4]}"
                items.append(formatted_item)
            
            # Update the listbox with the formatted items
            print_list(listbox, items)
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
##########################################################################################################
##########################################################################################################   
#THIRD OPTION OF THE MENU     

###################### PRINCIPAL MENU ######################################################################

window=tk.Tk()
window.geometry("800x800")
window.configure(bg="#333333")
window.resizable(False,False)

    #CREATION PAGES
menu = Frame(window,bg="#333333")
write = Frame(window,bg="#333333")
messages = Frame(window,bg="#333333")
modify = Frame(window,bg="#333333")

    #grid pages
menu.grid(row=0,column=0,sticky="nsew") #MENU 1
write.grid(row=0,column=0,sticky="nsew")
messages.grid(row=0,column=0,sticky="nsew")
modify.grid(row=0,column=0,sticky="nsew")


    
####################################################################################################
#########################   BUTTONS FOR THE PRINCIPAL MENU   #######################################
####################################################################################################
#function for the first menu

title1 = Label(menu,text="PRINCIPAL MENU",bg="#333333",fg="white")
title1.pack(pady=50,padx=325)

btn1= Button(menu,text="Write the message",bg="#333333",fg="white", width=15,command=lambda:write.tkraise())
btn1.pack(pady=10,padx=325)
    
btn2= Button(menu,text="The list of messages",bg="#333333",fg="white", width=15,command=lambda:messages.tkraise())
btn2.pack(pady=10,padx=325)

btn3= Button(menu,text="Update messages",bg="#333333",fg="white", width=15,command=lambda:modify.tkraise())
btn3.pack(pady=10,padx=325)

btn4= Button(menu,text="Exit",bg="#333333",fg="white", width=10,command=quit)
btn4.pack(pady=10,padx=325) #exit TO THE APP



####################################################################################################
###################### PAGE 1 ######################################################################
####################################################################################################
 
title=Label(write,text="Write your message",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

    #TO PRINT THE TEXT
label1 = Label(write,text="► Message ◄",bg="#333333",fg="white")
label1.pack()
entry=Entry(write, width=30)
entry.pack(pady=20)

label2 = Label(write,text="► Choose the number ◄",bg="#333333",fg="white")
label2.pack()
key=Entry(write, width=5)
key.pack(pady=20)

btn1=Button(write,text="Confirm",bg="#333333",fg="white", command=print_entry_text) #THE FUNCTION IS UP
btn1.pack(pady=50,padx=325)

label3 = Label(write,text="► Ciphertext ◄",bg="#333333",fg="white")
label3.pack()
label = Label(write, text="") 
label.pack(pady=30)

btn2=Button(write,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn2.pack(pady=50,padx=325)


####################################################################################################
###################### PAGE 2 ######################################################################
####################################################################################################

title=Label(messages,text="The list of all messages",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

#to show the list
listbox = tk.Listbox(messages, width=80, height=15)
listbox.pack(pady=20)
print_list(listbox,[])
######
update_button = tk.Button(messages, text="Update Listbox from DB", command=update_listbox)
update_button.pack(pady=10)

btn2=Button(messages,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn2.pack(pady=50,padx=325)

####################################################################################################
###################### PAGE 3 ######################################################################
####################################################################################################

title=Label(modify,text="Edit your message",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

delete=Button(modify,text="Delete",bg="#333333",fg="white")
delete.pack(pady=10)

edit=Button(modify,text="Edit",bg="#333333",fg="white")
edit.pack(pady=10)

btn1=Button(modify,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn1.pack(pady=50,padx=325)


####################################################################################################
###################### PEND PAGES ######################################################################
####################################################################################################

menu.tkraise() 
window.mainloop()




# COMMANDS FOR MYSQL
#DELETE FROM enigma WHERE id=;

#UPDATE enigma
#SET column1 = value1, column2 = value2, ...
#WHERE condition;