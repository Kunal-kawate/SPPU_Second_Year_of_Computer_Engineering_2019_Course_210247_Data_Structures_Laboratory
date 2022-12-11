'''
Write a pythonprogram to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores
'''

def display(First_Year_Percentage):
    print("Top Five Marks are-")
    for i in range(-5,0):
        print(First_Year_Percentage[i])

def selection_sort(First_Year_Percentage):
    for i in range(0, len(First_Year_Percentage)):
        for j in range(i+1,len(First_Year_Percentage)):
            if(First_Year_Percentage[i]>First_Year_Percentage[j]):
                temp=First_Year_Percentage[i]
                First_Year_Percentage[i]=First_Year_Percentage[j]
                First_Year_Percentage[j]=temp
    print("Selection Sort in Done!!")
    display(First_Year_Percentage)

def bubble_sort(First_Year_Percentage):
    count=1
    while(count<len(First_Year_Percentage)):
        for i in range(0,len(First_Year_Percentage)-count):
            if(First_Year_Percentage[i]>First_Year_Percentage[i+1]):
                temp=First_Year_Percentage[i]
                First_Year_Percentage[i]=First_Year_Percentage[i+1]
                First_Year_Percentage[i+1]=temp
        count=count+1
    print("Bubble Sort in Done!!")
    display(First_Year_Percentage)

# Mian Program
if __name__=="__main__":
    First_Year_Percentage=[]
    n=int(input("Enter the Number of Students: "))
    for i in range(0,n):
        percentage=float(input("Enter the Percentage of Roll No. {}: ".format(i+1)))
        First_Year_Percentage.append(percentage)
    
    while(True):
        print("\n-----------------------Menu-----------------------\n1)Perform Selection Sort\n2)Perform Bubble Sort\n3)Exit")
        choice=int(input("Enter your choice (From 1 to 3): "))
        if(choice==1):
            selection_sort(First_Year_Percentage)
        elif(choice==2):
            bubble_sort(First_Year_Percentage)
        elif(choice==3):
            print("Thank You For Using This Program!!")
            break
        else:
            print("Please Enter the Valid Choice!!")
    
<<<<<----------------------------------------OUTPUT-------------------------------------------------->>>>>>
    
PS C:\Users\Kunal\Desktop\DSL_LAB> python -u "c:\Users\Kunal\Desktop\DSL_LAB\try.py"
  
Enter the Number of Students: 6
Enter the Percentage of Roll No. 1: 45.12
Enter the Percentage of Roll No. 2: 12.36
Enter the Percentage of Roll No. 3: 96.15
Enter the Percentage of Roll No. 4: 99.12
Enter the Percentage of Roll No. 5: 75.49
Enter the Percentage of Roll No. 6: 48.26

-----------------------Menu-----------------------
1)Perform Selection Sort
2)Perform Bubble Sort
3)Exit
Enter your choice (From 1 to 3): 1
Selection Sort in Done!!
Top Five Marks are-
45.12
48.26
75.49
96.15
99.12

-----------------------Menu-----------------------
1)Perform Selection Sort
2)Perform Bubble Sort
3)Exit
Enter your choice (From 1 to 3): 2
Bubble Sort in Done!!
Top Five Marks are-
45.12
48.26
75.49
96.15
99.12

-----------------------Menu-----------------------
1)Perform Selection Sort
2)Perform Bubble Sort
3)Exit
Enter your choice (From 1 to 3): 3
Thank You For Using This Program!!

PS C:\Users\Kunal\Desktop\DSL_LAB>
