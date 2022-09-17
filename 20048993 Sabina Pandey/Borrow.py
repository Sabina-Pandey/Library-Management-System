# importing all the necessary requirements
import dt
import ListSplit
import os

# Defining borrowBook with the name of the borrower
def borrowBook():
    while(True):
        firstName = input(" \nEnter your first name:\n")
        if firstName.isalpha():
            break
        print("Please enter valid name only!!")

    while(True):
        lastName = input(" \nEnter your last name:\n" )
        if lastName.isalpha():
            break
        print("Please enter valid name only!!")
           
       # Creating files for borrower    
    t = os.path.join('Borrow', "Borrow-"+firstName+lastName+ ".txt")
    s = os.path.join('Borrow', "File-"+firstName+lastName+ ".txt")
    u = os.path.join('Borrow', 'Receipt-'+firstName+lastName+".txt")

    if not(os.path.isfile(s)):
        with open(s, "w") as g:
            pass

    loop = True
    count = 0
    total = 0.0
    while loop == True:
        try:   
            try:
                with open (s, "r") as f:
                    r = f.read()
                    
                    # Displays all the available books and asks the users to choose from their
                print("\n\nEnter the number of the book that you want to borrow\n")
                print('+'+'-'* 80+'+')
                print(f'| {"S.N.":<5} | {"Book Name":<25} | {"Author Name":<20} | {"Quantity":<10} |  Price |')
                print('+'+'-'* 80+'+')
                for i in range(len(ListSplit.bookname)):
                    print(f'| {str(i+1)+".":<5} | {ListSplit.bookname[i]:<25} | {ListSplit.authorname[i]:<20} | {ListSplit.quantity[i]:<10} |  {"$"+ListSplit.cost[i]:5} |')
                print('+'+'-'* 80+'+')

                a = int(input())-1

                if(ListSplit.bookname[a] in r):
                    print("You cannot borrow same book twice.")
                    loop = False
                    break
        
                   # Stock available for the choosen books  
                if(int(ListSplit.quantity[a])>0):
                    print("\nBook is available\n")

                    # Condition to avoid for making new files whenever loop repeats
                    if count == 0:
                        if os.path.isfile(t):
                            with open(t , "a") as f:
                                f.write("\n\t\t\t\t Date: " + dt.getDate()+"\n\n")
                                f.write("S.N. \t\t Bookname \t\t\t Authorname \t\t\t Cost \n")
                        else:
                            with open(t, "w") as f:
                                f.write("\t\t\t\t Library Management System  \n")
                                f.write("\t\t\t\t Borrowed By: "+ firstName+" "+lastName+"\n")
                                f.write("\n\n\t\t\t\t Date: " + dt.getDate()+"\n\n")
                                f.write("S.N. \t\t Bookname \t\t\t Authorname \t\t\t Cost \n")
                        
                        with open(u, "w") as f:
                            f.write("\t\t\t\t Library Management System  \n")
                            f.write("\t\t\t\t Borrowed By: "+ firstName+" "+lastName+"\n")
                            f.write("\n\n\t\t\t\t Date: " + dt.getDate()+"\n\n")
                            f.write("S.N. \t\t Bookname \t\t\t Authorname \t\t\t Cost \n")

                    count = count + 1

                    total += float(ListSplit.cost[a])
                    
                    # Details of the borrowed books shown in the text files
                    with open(t,"a") as f:
                        f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t\t  "+ListSplit.authorname[a]+"\t\t\t  "+ListSplit.cost[a] +"\n")
                    
                    with open(u,"a") as f:
                        f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t\t  "+ListSplit.authorname[a]+"\t\t\t  "+ListSplit.cost[a] +"\n")
                    
                    with open(s,"a") as f:
                        f.write(ListSplit.bookname[a]+"\n")

                    ListSplit.quantity[a] = int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(len(ListSplit.bookname)):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")

                            # For books which are out of stock
                else:
                    print("Book is not available")
                    with open(t , "a") as f:
                        f.write("\n\t\t\t\t\t\t\t\t\t   Total: " + str(total))
                        f.write("\n--------------------------------------------------------------------------------------\n")

                    print ("Thank you for borrowing books from us. ")
                    print("")
                    loop = False
                    borrowBook()

                   # To select more books to borrow
                choice = input("Do you want to borrow more books? However you cannot borrow same book twice. Press 'y' for Yes and 'n' for No: ")
                if(choice.upper() == "Y"):
                    continue
                   
                   # To display the total amount after borrowing the book
                elif (choice.upper() == "N"):
                    with open(t , "a") as f:
                        f.write("\n\t\t\t\t\t\t\t\t\t   Total: " + str(total))
                        f.write("\n--------------------------------------------------------------------------------------\n")
                    
                    with open(u , "a") as f:
                        f.write("\n\t\t\t\t\t\t\t\t\t   Total: " + str(total))
                        f.write("\n--------------------------------------------------------------------------------------\n")
                    
                    with open(u, 'r') as f:
                        print('\n'+f.read())

                     # Thank you message
                    print ("Thank you for visiting our Library. Plese visit again.")
                    print("")
                    loop = False
                else:
                    print("Please choose as instructed")
                
            except IndexError:
                print("")
                print("Please choose book according to their number.")
                
        except ValueError:
            print("")
            print("Please choose as suggested.")