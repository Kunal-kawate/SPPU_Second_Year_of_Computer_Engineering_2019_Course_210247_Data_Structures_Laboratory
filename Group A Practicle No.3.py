'''
Write a Python program for department library which has N books, write functions for
following:
a) Delete the duplicate entries
b) Display books in ascending order based on cost of books
c) Count number of books with cost more than 500.
d) Copy books in a new list which has cost less than 500.
'''

def deleteDuplicate(booksList):
    tempList=[]
    for item in booksList:
        if(item not in tempList):
            tempList.append(item)
    return tempList

def selectionSort(booksList):
    for i in range(0,len(booksList)):
        for j in range(i+1,len(booksList)):
            if(booksList[i][1]>booksList[j][1]):
                temp=booksList[i]
                booksList[i]=booksList[j]
                booksList[j]=temp
    
def displayBooks(booksList):
    print("\n--------------------------------BOOKS------------------------------\n")
    for i in range(0,len(booksList)):
        item=booksList[i]
        name=item[0]
        price=item[1]
        print("Book Name: ",name,"  Price: ",price)

def lessPriceBook(booksList):
    lessPriceBookList=[]
    for item in booksList:
        if(item[1]<500):
            lessPriceBookList.append(item)
    return lessPriceBookList

if __name__=="__main__":

    booksList=[]
    n=int(input("Enter the number of books: "))
    for i in range(n):
        bookName=input("Enter the name of book: ")
        bookPrice=int(input("Enter the price: "))
        booksList.append([bookName.lower(),bookPrice])

    condition=True

    while(condition):
        choice=int(input("\n--------------------------------MENU------------------------------\n1)Delete the duplicate entries\n2)Display books\n3)Count number of books with cost more than 500.\n4)list of books which has cost less than 500.\n5)Exit\nEnter your choice: "))

        if(choice==1):
            booksList=deleteDuplicate(booksList)
        elif(choice==2):
            selectionSort(booksList)
            displayBooks(booksList)
        elif(choice==3):
            lessPriceBookList=lessPriceBook(booksList)
            print("\nNumber of books with cost more than 500: ",len(booksList)-len(lessPriceBookList))
        elif(choice==4):
            lessPriceBookList=lessPriceBook(booksList)
            if(len(lessPriceBookList)==0):
                print("\nNo books which has cost less than 500!!")
            else:
                displayBooks(lessPriceBookList)
        elif(choice==5):
            condition=False
        else:
            print("\nPlease Enter Valid Choice!!!\n")
        
