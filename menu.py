from nodeclass import Node
from chord import hashlib
import linecache
import sys
import os
from fun import * 
def menu():
    print("------------------- Menu: -------------------\n")
    print("1 --> ADD node & Key\n")
    print("2 --> Delete node& Key\n")
    print("3 --> show finger table\n")
    print("4 --> print chord ring\n")
    print("5 --> search node & key \n")
    print("6 --> Print values of Nodes\n")
    print("7 --> Exit\n")
    choise = input("choose one:--> ")

    return choise
    

def main():
    while True:
        choise = menu()

        if choise == '1':
            givenum=input("give the id of the node")
            num=hash(givenum,ring_size)
            while num>=ring_size:
                num=int(input("give smaller id than {}".format(ring_size)))
            check=True
            for item in sortli:
                if item.id_ == num:
                    check == False
            if check == True: 
                sortli = func(sortli,num) #adding func
            enableprint()
            print('node added: {}'.format(num))

        elif choise == '2':
            delete=input("give the id of the node:")
            #delete func
        
        elif choise == '3':
            print("\n\n\n")
            for item in sortli:
                print("Node:{}".format(item))
                
        elif choise == '4':
            for item in sortlist:
                print(item.predecessor,end ='\t')
                print(item, end='\t')
                print(item.succesor)

        elif choise == '5':
            nodeval = int(input("give the node number you'd ou like to find"))
            keyval = input("give the key you'd ou like to find")
            find = int(hash(keyval,ring_size))
            #searching func

        elif choise == '6':
             print("your ring now is:\n")
             for item in sortli:
                 print("values of node {} are:".format(item.id))
                 print(item.Nodevalues)    

        elif(choise == '7'):
           sys.exit("bye!")



if __name__ == '__main__':
    print("---------------------- Welcome to DHT CHORD ----------------------\n")
    main()
