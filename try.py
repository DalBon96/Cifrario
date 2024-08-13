
#Le classi sono OGGETTI
class Persona:

    #COSTRUTTORE / funzione (Automatica)
    def __init__(self,nome,cognome): #self == riferimento a se stesso
        self.nome = nome
        self.cognome = cognome
    #prende i parametri

    #Metodo
    def saluta(self):
        print("ciao sono " + self.nome)

    #######################
#istanza == quella determinata persona

class Insegnante(Persona): #Classe estende Persona
    def __init__(self,nome,cognome,materia):
        super().__init__(nome,cognome)
        self.materia = materia
    #pass #è un check
    #prende lo stesso costruttore

    def saluta(self):
        print("buongiorno sono "+ self.nome + " " + self. cognome ) #OVERWRITING

    def dati_voto(self):
        print("Bravo un bel 8")

persona1 = Persona("Luca","Rossi")
insegnante1 = Insegnante("Matteo","Rossi","Matematica")

insegnante1.saluta()
insegnante1.dati_voto()