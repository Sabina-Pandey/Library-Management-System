#importing all the necessary requirements
import ListSplit
import Borrow
import Return

def start():
    while(True):
        # Main Menu
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Borrow a book\n")
        print("Enter 2. To return a book\n")
        print("Enter 3. To exit\n")

        try:
            # Choices to select if the user want to borrow, return or exit
            a = int(input("Select a choice from 1-3: "))
            print()
            
            # Calls the borrowBook function from borrow program
            if(a==1):
                ListSplit.listSplit()
                Borrow.borrowBook()

            # Calls the returnBook function from return program
            elif(a==2):
                ListSplit.listSplit()
                Return.returnBook()
            
            # Closes the program with thank you message
            elif(a==3):
                print("Thank you for visiting our Library. Plese visit again.")
                break
            else:
                print("Please enter a valid choice from 1-3\n")
        except ValueError:
            print("\nPlease input as suggested.\n")
start()
