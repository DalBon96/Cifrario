import tkinter 
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

            ##########################
                break  # Exit the loop if conversion is successful
            except Exception as e:
        # Handle the error and display a message box
                messagebox.showerror("Error", f"Invalid Input: {e}")
                entry_key.delete(0, Tk.END)
    
    text2 = list(entry_text) #I create the Array
    #new_key=int(key) # i transform the string to int
    ascii_numbers = [ord(char)+int(entry_key) for char in text2] #i transform the values in the list in ASCII and i sum the KEY
    
        #i transform from ASCII to list of letters
        #and create the edit string
    new_list=[]
    for value in ascii_numbers:
        new_list.append(chr(value))
    #print(''.join(new_list)) #the new string is edit within a key
    label.config(text=''.join(new_list))




###################### MENU 1 ######################################################################

window=tkinter.Tk()
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

btn1= Button(menu,text="menu 1",bg="#333333",fg="white", width=10,command=lambda:page1.tkraise())
btn1.pack(pady=10,padx=325)
    
btn2= Button(menu,text="menu 2",bg="#333333",fg="white", width=10,command=lambda:page2.tkraise())
btn2.pack(pady=10,padx=325)

btn3= Button(menu,text="menu 3",bg="#333333",fg="white", width=10,command=lambda:page3.tkraise())
btn3.pack(pady=10,padx=325)

btn4= Button(menu,text="Exit",bg="#333333",fg="white", width=10,command=quit)
btn4.pack(pady=10,padx=325) #exit TO THE APP

####################################################################################################

###################### MENU 1 ######################################################################
 
title=Label(page1,text="This is page 1",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

    #TO PRINT THE TEXT
entry=Entry(page1, width=30)
entry.pack(pady=20)

key=Entry(page1, width=5)
key.pack(pady=20)


btn1=Button(page1,text="Confirm",bg="#333333",fg="white", command=print_entry_text) #THE FUNCTION IS UP
btn1.pack(pady=50,padx=325)


label = Label(page1, text="") 
label.pack(pady=30)

btn2=Button(page1,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn2.pack(pady=50,padx=325)


###################### MENU 2 ######################################################################

title=Label(page2,text="This is page 2",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

btn1=Button(page2,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn1.pack(pady=50,padx=325)

###################### MENU 3 ######################################################################

title=Label(page3,text="This is page 3",bg="#333333",fg="white")
title.pack(pady=50,padx=325)

btn1=Button(page3,text="Come back in MENU",bg="#333333",fg="white",command=lambda:menu.tkraise())
btn1.pack(pady=50,padx=325)



menu.tkraise() 
window.mainloop()


