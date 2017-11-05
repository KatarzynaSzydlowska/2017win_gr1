# !/usr/bin/python
from cmd import Cmd
import datetime

client_dictionary = {}
bank_dictionary = {}


class Client:
    def __init__(self, name, bank_balance):
        self.name = name
        self.bank = ""
        self.bank_balance = bank_balance
        client_dictionary[name] = self


class Bank:
    def __init__(self, name):
        self.name = name
        bank_dictionary[name] = self
        self.bank_client = {}

    def add_client(self, client):
        client.bank = self.name
        self.bank_client[client.name] = client

    def cash_input(self, client_name, payment):
        if client_name in self.bank_client.keys():
            client = self.bank_client[client_name]
            client.bank_balance += payment
            myDump.update_dump(client)
            return str('Cash input to: ' + client.name + ' ended with success')
        else:
            return str('Failed: ' + client_name + ' is not a client of a bank: ' + self.name)

    def withdrawal(self, client_name, withdrawal):
        if client_name in self.bank_client.keys():
            client = self.bank_client[client_name]
            client.bank_balance -= withdrawal
            myDump.update_dump(client)
            return str('Withdrawal from: ' + client.name + ' ended with success')
        else:
            return str('Failed: ' + client_name + ' is not a client of a bank: ' + self.name)

    def transfer_from_a_to_b(self, client_a_name, client_b_name, money):
        if client_a_name in self.bank_client.keys():
            client_a = self.bank_client[client_a_name]
            if client_b_name in client_dictionary.keys():
                client_b = client_dictionary[client_b_name]
                client_a.bank_balance -= money
                client_b.bank_balance += money
                myDump.update_dump(client_a)
                myDump.update_dump(client_b)
                return str('Transfer ended with success.')
            else:
                return str('There is no client with name: ' + client_b_name)
        else:
            return str('Failed: ' + client_a_name + ' is not a client of a bank: ' + self.name)


class Dump:
    def __init__(self):
        self.name = str('dumpFile' + str(datetime.datetime.now()))
        dumpfile = open(str(self.name) + '.txt', 'w')
        dumpfile.write('Dump created on: ' + str(datetime.datetime.now()) + '\n\n')
        dumpfile.write('Dump updated on: ' + str(datetime.datetime.now()) + '\n')
        dumpfile.close()

    def update_dump(self, client):
        dumpfile = open(str(self.name) + '.txt', 'r')
        dumplines = dumpfile.readlines()
        dumped = False
        for i, line in enumerate(dumplines):
            if client.name in line:
                dumplines[i] = str(
                    'Client: ' + str(client.name) + ' Bank balance: ' + str(client.bank_balance) + ' bank: ' + str(
                        client.bank) + '\n')
                dumped = True
        if not dumped:
            dumplines.append(str(
                'Client: ' + str(client.name) + ' Bank balance: ' + str(client.bank_balance) + ' bank: ' + str(
                    client.bank) + '\n'))
        dumplines[2] = str('Dump updated on: ' + str(datetime.datetime.now()) + '\n')
        dumpfile.close()
        dumpfile = open(str(self.name) + '.txt', 'w')
        dumpfile.writelines(dumplines)
        dumpfile.close()


class MyPrompt(Cmd):
    def help(self):
        """Type: help <option>"""

    def do_show_options(self):
        """Options: \n1)Cash input (type: cash_input <your_bank> <your_name> <money>)
                    \n2)Withdrawal (type: withdrawal <your_bank> <your_name> <money>)
                    \n3)Transfer from A to B (type: transfer <your_bank> <your_name> <money>) """

    def do_cash_input(self, argv):
        """Cash input: (type: cash_input <your_bank> <your_name> <money>"""
        my_list = argv.split()
        bank_name = my_list[0]
        name = my_list[1]
        cash = int(my_list[2])
        if bank_name in bank_dictionary.keys():
            print str(bank_dictionary[bank_name].cash_input(name, cash))
        else:
            print "Failed"

    def do_withdrawal(self, argv):
        """Withdrawal: (type: withdrawal <your_bank> <your_name> <money>"""
        my_list = argv.split()
        bank_name = my_list[0]
        name = my_list[1]
        cash = int(my_list[2])
        if bank_name in bank_dictionary.keys():
            print str(bank_dictionary[bank_name].withdrawal(name, cash))
        else:
            print "Failed"

    def do_transfer(self, argv):
        """Transfer: (type: transfer <your_bank> <your_name> <clientB_name> <money>"""
        my_list = argv.split()
        bank_name = my_list[0]
        name_a = my_list[1]
        name_b = my_list[2]
        cash = int(my_list[3])
        if bank_name in bank_dictionary.keys():
            print str(bank_dictionary[bank_name].transfer_from_a_to_b(name_a, name_b, cash))
        else:
            print "Failed"

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit


if __name__ == '__main__':
    myDump = Dump()
    myBank1 = Bank("mBank")
    myBank2 = Bank("kBank")

    clientA = Client("Kowal", 1000)
    clientB = Client("Nowak", 2000)
    clientC = Client("Cowak", 2500)
    myBank1.add_client(clientA)
    myBank1.add_client(clientB)
    myBank2.add_client(clientC)

    print myBank1.cash_input("Kowal", 1000)
    print myBank1.cash_input("Kowal", 3000)
    print myBank1.cash_input("Nowak", 2000)
    print myBank1.cash_input("Cowak", 2000)
    print myBank2.cash_input("Cowak", 2000)

    print myBank1.withdrawal("Kowal", 1000)
    print myBank1.withdrawal("Nowak", 2000)
    print myBank1.withdrawal("Cowak", 2000)
    print myBank2.withdrawal("Cowak", 2000)

    print myBank1.transfer_from_a_to_b("Kowal", "Cowak", 505)

    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop("""Welcome to Bank Simulator! Options:
        1)Cash input (type: cash_input <your_bank> <your_name> <money>)
        2)Withdrawal (type: withdrawal <your_bank> <your_name> <money>)
        3)Transfer from A to B (type: transfer <your_bank> <your_name> <money>) """)
