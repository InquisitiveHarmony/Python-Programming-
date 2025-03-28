from linkedlist import LinkedList

def add_client():
    my_list = LinkedList()
    print(input("Provide the client's name: "))
    print(input("Provide the client's phone number: "))
    print(input("Provide the client's D.O.B. in MM/DD/YYYY: "))
    my_list.append(input)
    print("You've added a new client!")
def display_clients():
    my_list = LinkedList()
    __str__(self)
def search_client():
    my_list = LinkedList()
    print(my_list)
    print(input("Enter client name: "))
    if input in my_list:
        print(input, "is in the list")
    else:
        print(input, "is not in the list")
def delete_client():
        print("Client Deleted")


def menu():
    print("Type the number for the action you wish to perform and hit Enter.")
    print("1. Add a new client")
    print("2. Display a list of all current clients")
    print("3. Search for a client")
    print("4. Delete a client")
    print("5. Quit")
    userInput = print(input("What do you want to do? "))
    
    if userInput == 1: 
        add_client()
    elif userInput == 2:
        display_clients()
    elif userInput == 3:
        search_client()
    elif userInput == 4:
        delete_client()
    elif userInput == 5:
         exit()
    else:
         print("Sorry, that is not an allowed action.")
         menu()

menu()