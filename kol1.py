#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#!/usr/bin/python

class Client:
    def __init__(self, bank, name, cash):
        self.bank = bank
        self.name = name
        self.cash = cash

class Bank:
    clientCount = 0
    def __init__(self, name):
        self.name = name

    def addClient(self,client):
        #client = Client(self.name, name, cash)
    
    def cashInput(client, money):
        client.cash += money

    def withdrawal(client, money):
        client.cash -= money
        
    def transferFromAToB(clientA, clientB, money):
        clientA.cash -= money
        clientA.cash += money


myBank = Bank("mBank")
myBank.addClient(clientA)
clientA = Client("mBank","Kowalski",3432)
