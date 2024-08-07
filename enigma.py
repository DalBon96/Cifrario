class Enigma:
    def __init__(self,message,key): #first function???
        self.message=message
        self.key=key

    def print_message(self):
        return f"{self.message}, {self.key}is now sitting."
    

    

message=input("Choose a message...")
key=input("Choose a key...")
cipher=Enigma(message,key)

print(cipher.print_message())
        