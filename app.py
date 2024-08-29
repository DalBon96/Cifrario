import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector #MYSQL

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
    save_data(entry_text,save_value)

#Method to save the text and the EDIT test  FROM print_entry_text()
def save_data(text,text2):
    data=db.cursor()
    data.execute("INSERT INTO enigma (message,new_message) VALUES (%s,%s)",(text,text2))
    db.commit()


#SECOND OPRTION OF THE MENU
#SHOW THE LIST
def print_list(listbox):
    listbox.delete(0, tk.END)

    data=db.cursor()
    data.execute("SELECT * FROM enigma")

    for item in data:
        listbox.insert(tk.END, item)
        

    db.commit()
         




###################### MENU 1 ######################################################################

window=tk.Tk()
window.geometry("800x800")
window.configure(bg="#333333")
window.resizable(False,False)

    #CREATION PAGES
menu= Frame(window,bg="#333333")
page1 = Frame(window,bg="#333333")
page2 = Frame(window,bg="#333333")
page3 = Frame(window,bg="#333333")

    #grid pages
menu.grid(row=0,column=0,sticky="nsew") #MENU 1
page1.grid(row=0,column=0,sticky="nsew")
page2.grid(row=0,column=0,sticky="nsew")
page3.grid(row=0,column=0,sticky="nsew")


    
####################################################################################################
#function for the first menu

title1 = Label(menu,text="PRINCIPAL MENU",bg="#333333",fg="white")
title1.pack(pady=50,padx=325)

btn1= Button(menu,text="Write the message",bg="#333333",fg="white", width=15,command=lambda:page1.tkraise())
btn1.pack(pady=10,padx=325)
    
btn2= Button(menu,text="The list of messages",bg="#333333",fg="white", width=15,command=lambda:page2.tkraise())
btn2.pack(pady=10,padx=325)

btn3= Button(menu,text="Update messages",bg="#333333",fg="white", width=15,command=lambda:page3.tkraise())
btn3.pack(pady=10,padx=325)

btn4= Button(menu,text="Exit",bg="#333333",fg="white", width=10,command=quit)
btn4.pack(pady=10,padx=325) #exit TO THE APP

####################################################################################################

###################### PAGE 1 ######################################################################
 
title=Label(page1,text="Write your message",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

    #TO PRINT THE TEXT
label1 = Label(page1,text="► Message ◄",bg="#333333",fg="white")
label1.pack()
entry=Entry(page1, width=30)
entry.pack(pady=20)

label2 = Label(page1,text="► Choose the number ◄",bg="#333333",fg="white")
label2.pack()
key=Entry(page1, width=5)
key.pack(pady=20)


btn1=Button(page1,text="Confirm",bg="#333333",fg="white", command=print_entry_text) #THE FUNCTION IS UP
btn1.pack(pady=50,padx=325)


label3 = Label(page1,text="► Ciphertext ◄",bg="#333333",fg="white")
label3.pack()
label = Label(page1, text="") 
label.pack(pady=30)

btn2=Button(page1,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn2.pack(pady=50,padx=325)


###################### PAGE 2 ######################################################################

title=Label(page2,text="The list of all messages",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

#to show the list
listbox = tk.Listbox(page2, width=80, height=15)
listbox.pack(pady=20)
print_list(listbox)
######

btn2=Button(page2,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn2.pack(pady=50,padx=325)

###################### PAGE 3 ######################################################################

title=Label(page3,text="This is page 3",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

btn1=Button(page3,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn1.pack(pady=50,padx=325)



menu.tkraise() 
window.mainloop()


