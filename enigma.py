class Enigma:
    def __init__(self,text,key): #Costruttore
        self.text = text
        self.key = key

    # Function to check if the KEY is a INT
    def check_key(self):
        while True:
            try:
            # Convert the input to an integer
                int(self.key)

                print("The key is a Number")
                self.print_message()
            ##########################
                break  # Exit the loop if conversion is successful
            except ValueError:
            # Handle the case where conversion fails
                print("That's not a number. Please try again....")
                self.key = input("Enter a value: ")

    
    
    def print_message(self):
        print("---------------")
        print("Your message is : " + self.text)
        print("The key is : "+self.key)
        print("---------------")

    def split_text(self,text,key):
        text2 = list(text) #I create the Array
        new_key=int(key) # i transform the string to int
        ascii_numbers = [ord(char)+new_key for char in text2] #i transform the values in the list in ASCII and i sum the KEY
        print(ascii_numbers)

        #i transform from ASCII to list of letters
        #and create the edit string
        new_list=[]
        for value in ascii_numbers:
            new_list.append(chr(value))
        print(''.join(new_list)) #the new string is edit within a key

#########---END CLASS----------



#INPUT FUNCTIONS.......
#start the programm from here
text=input()
key=input()

cipher = Enigma(text,key)
cipher.check_key()
cipher.split_text(text,key)

    

        

        