#Declaring all the global variables
def listSplit():
    global bookname
    global authorname
    global quantity
    global cost

    # Initializing the empty lists
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]

    # Reads the stock.txt files
    with open("stock.txt","r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))
                ind+=1