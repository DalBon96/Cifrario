#############################
class Enigma:
    def __init__(self,message,key): #first function???
        self.message=message
        self.key=key

    def print_value(self):
        self.check_key(self)
        return f"{self.message}, {self.key} these are the values."
    
    def check_key(self):
        while True:
            try:
            # Try to convert the input to an integer
                int(self.key)
                print("the values is a int")
                break
            except ValueError:
    #       # Handle the case where conversion fails
                print("That's not a number. Please try again....")
                self.key = input("Enter a value: ")

#########---END CLASS----------



#INPUT FUNCTIONS.......
message=input("Choose a message...")
key=input("Choose the key (1-10)...")

#I CALL THE CLASS.......
cipher=Enigma(message,key) 
print(cipher.print_value())
##########################
    

    

        

        