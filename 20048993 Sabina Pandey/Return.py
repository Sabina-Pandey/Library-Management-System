# importing all the necessary requirements
import ListSplit
import dt
import os

# Definining returned book with the name of returner
def returnBook():
    firstName = input("\nEnter your first name:\n")
    lastName = input("\nEnter your last name:\n")
    
    # Creating files for returner
    a = os.path.join("Borrow","Borrow-"+firstName + lastName +".txt")
    b = os.path.join("Return","Return-" + firstName + lastName +".txt")
    d = os.path.join("Return","Receipt-"+firstName+lastName+".txt")
   
    try:
        with open(a,"r") as f:
            f.read()

    except:
        print("Please enter valid name only!!")
        returnBook()

    c = os.path.join('Borrow', "File-"+ firstName + lastName + ".txt")

    loop = True
    count = 0
    total = 0.0
    fine = 0.0
    while loop == True:
        print("\nPlease select an option below:\n")
        # borrowerfile prints the books borrowed
        global bookname
        global date
        bookname=[]
        date=[]

        with open(c,"r") as f:
            lines = f.readlines()
            lines = [x.strip('\n') for x in lines]
            for i in range(len(lines)):
                ind = 0
                for a in lines[i].split(','):
                    if(ind == 0):
                        bookname.append(a)
                    elif(ind == 1):
                        date.append(a)
                    ind += 1

        for i in range(len(bookname)):
            print(str(i+1)+ ' --------------- ' + bookname[i])
        
        try:
            a = int(input())-1

            with open ('Stock.txt', 'r') as f:
                for num, line in enumerate(f):
                    if bookname[a] in line:
                        x = num
                        break
            
            # Condition to avoid for making new files whenever loop repeats
            if count == 0:
                if os.path.isfile(b):
                    with open(b,"a") as f:
                        f.write("\t\t\t Date: " + dt.getDate()+"\n\n")
                        f.write("S.N.\t\t Bookname\t\t\t Cost\n")
                else:
                    with open(b,"w")as f:
                        f.write("\t\t\t Library Management System \n")
                        f.write("\t\t\t Returned By: "+ firstName + lastName+"\n")
                        f.write("\n\t\t\t Date: " + dt.getDate()+"\n\n")
                        f.write("S.N.\t\t Bookname\t\t\t Cost\n")
                with open(d,"w")as f:
                    f.write("\t\t\t Library Management System \n")
                    f.write("\t\t\t Returned By: "+ firstName + lastName+"\n")
                    f.write("\n\t\t\t Date: " + dt.getDate()+"\n\n")
                    f.write("S.N.\t\t Bookname\t\t\t Cost\n")

            count = count + 1

            # showing details of the borrowed books in the text files
            with open(b,"a") as f:
                f.write(str(count)+"\t\t"+ListSplit.bookname[x]+"\t\t\t $"+ListSplit.cost[x]+"\n")
            
            with open(d,"a") as f:
                f.write(str(count)+"\t\t"+ListSplit.bookname[x]+"\t\t\t $"+ListSplit.cost[x]+"\n")
            total += float(ListSplit.cost[x])

            ListSplit.quantity[x]=int(ListSplit.quantity[x]) + 1
            with open("Stock.txt","w+") as f:
                for i in range(len(ListSplit.bookname)):
                    f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")

                # Asking the user if the book is returned date expired    
            print("Is the book return date expired? Press 'y' for Yes and 'n' for No: ")
            stat = input()
            if(stat.upper() == "Y"):
                print("By how many days was the book returned late?")
                day = int(input())
                fine = 2 * day
                with open(b,"a") as f:
                    f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
                total = total + fine

            with open(c, 'r') as f:
                contents = f.readlines()
            contents.pop(a)
            with open(c, 'w') as f:
                contents = ''.join(contents)
                f.write(contents)
            
            # Asking the user to return more books if they want to
            choice = str(input("Do you want to return more books? Press 'y' for Yes and 'n' for No: "))

            if choice.upper() == 'Y':
                continue
               
               # To display the total amount after returning the book
            elif (choice.upper() == "N"):
                print("Final Total: "+ "$"+str(total))
                with open(b,"a")as f:
                    f.write("\t\t\t\t\tFine: $"+ str(fine)+'\n')
                    f.write("\t\t\t\t\tTotal: $"+ str(total))
                    f.write("\n ----------------------------------------------------------------- \n")
                
                with open(d,"a")as f:
                    f.write("\t\t\t\t\tFine: $"+ str(fine)+'\n')
                    f.write("\t\t\t\t\tTotal: $"+ str(total))  
                    f.write("\n ----------------------------------------------------------------- \n")
                
                with open(d,"r") as f:
                    print(f.read())
                
                # Thank you message
                    loop = False
                print("Thank you for visiting our Library. Plese visit again.\n\n")
            
            else:
                print("Please choose as instructed.")

        except IndexError:
            print("Please choose as suggested.")