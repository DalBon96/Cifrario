import tkinter as tk 

class MyApp2(object): 

    def __init__(self, parent): 

        self.root2 = parent 

        self.root2.title("Main frame") 
 
        self.frame = tk.Frame(parent) 

        self.frame.pack() 

        btn = tk.Button(self.frame, text="Open Frame", command=self.openFrame) 

        btn.pack()  
                                                         
    def openFrame(self):
        pass

root2 = tk.Tk()

root2.geometry("800x600")
                                                  
#app = MyApp2(root2)
                                             
root2.mainloop()