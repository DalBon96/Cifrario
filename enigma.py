#############################
class Enigma:
    def __init__(self,message,key): #first function???
        self.message=message
        self.key=key

    def print_message(self):
        return f"{self.message}, {self.key} is now sitting."

#########---END CLASS----------



#INPUT FUNCTIONS.......
def menu():
    message=input("Choose a message...")
    key=input("Choose the key (1-10)...")
    while True:
        try:
            # Try to convert the input to an integer
            int(key)

            #I CALL THE CLASS.......
            cipher=Enigma(message,key)
            print(cipher.print_message())
            ##########################

            break  # Exit the loop if conversion is successful
        except ValueError:
            # Handle the case where conversion fails
            print("That's not a number. Please try again....")
            key = input("Enter a value: ")

    

        
    

menu()

        