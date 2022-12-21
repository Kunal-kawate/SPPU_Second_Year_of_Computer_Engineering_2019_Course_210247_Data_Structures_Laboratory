'''
Write a python program to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using quick sort and display
top five scores.
'''

def acceptPercentage(percentage):
    n=int(input("\nEnter the Number of Students: "))
    for i in range(0,n):
        userInput=float(input("Enter the Percentage of Roll No.{}: ".format(i+1)))
        percentage.append(userInput)

def topFiveScore(percentage):
    if(len(percentage)>=5):
        print("\nTop Five Scores are-")
        indexNumber=-1
        for k in range(0,5):
            print(percentage[indexNumber-k])
    else:
        print("Enter at Least Five Students Percentage!")

#QuickSort Code-
def swap(percentage,i,j):
    temp=percentage[i]
    percentage[i]=percentage[j]
    percentage[j]=temp

def partition(percentage,L,R):
    pivot=percentage[R]
    i=L-1
    for j in range(L,R):
        if(percentage[j]<pivot):
            i=i+1
            swap(percentage,i,j)
    swap(percentage,i+1,R)
    return i+1

def quickSort(percentage,L,R):
    if(L<R):
        pivotIndex=partition(percentage,L,R)
        quickSort(percentage,pivotIndex+1,R)
        quickSort(percentage,L,pivotIndex-1)

#Main Program
if __name__=="__main__":
    percentage=[]
    while(True):
        print("\n-----------------MENU------------------\n1)Accept the Percentage.\n2)Perform QuickSort.\n3)Display Top Five Scores.\n4)Exit")
        choice=input("\nEnter Your Choice(From 1 to 4): ")
        if(choice=='1'):
            acceptPercentage(percentage)
        elif(choice=='2'):
            L=0
            R=len(percentage)-1
            quickSort(percentage,L,R)
            print("\nQuickSort Done.....")
        elif(choice=='3'):
            topFiveScore(percentage)
        elif(choice=='4'):
            print("\nThank You for Using This Program.\n")
            break
        else:
            print("Please Enter the Valid Choice!!")
