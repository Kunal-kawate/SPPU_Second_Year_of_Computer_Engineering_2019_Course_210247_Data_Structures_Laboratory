'''
       Write a python program to maintain club members, sort on roll numbers in ascending
order. Write function “Ternary_Search” to search whether particular student is member
of club or not. Ternary search is modified binary search that divides array into 3 halves
instead of two.
'''

def Accept_Students_Roll_No(studentsRollNo):
    n=int(input("Enter the Number of Students: "))
    for i in range(0,n):
        rollNo=int(input("Enter the Roll No. :"))
        if(rollNo not in studentsRollNo):
            studentsRollNo.append(rollNo)
        else:
            print("Roll No. {} is already member of the Club....".format(rollNo))
            break

def sortingFunction(studentsRollNo):
    for j in range(0,len(studentsRollNo)):
        for k in range(j,len(studentsRollNo)):
            if(studentsRollNo[j]>studentsRollNo[k]):
                temp=studentsRollNo[j]
                studentsRollNo[j]=studentsRollNo[k]
                studentsRollNo[k]=temp
    print("Sorting is Done!!!","\n\n")

def displayStudentsRollNo(studentsRollNo):
    for l in studentsRollNo:
        print(l)
    print("\n\n")

def Non_Recursive_Ternary_Search(studentsRollNo):
    val=int(input("Enter the Roll No. to be search: "))
    firstIndex=0
    lastIndex=(len(studentsRollNo)-1)
    if(val==studentsRollNo[lastIndex]):
        print("Roll No. {} is found at index {} ".format(val,lastIndex))
        print("Roll No. {} is member of the club.".format(val),"\n\n")
    elif(val in studentsRollNo):
        while(firstIndex<=lastIndex):
            m1=int((firstIndex+lastIndex)/3)
            m2=int(m1+m1)
            if(studentsRollNo[m1]==val):
                print("Roll No. {} is found at index {} ".format(val,m1))
                print("Roll No. {} is member of the club.".format(val),"\n\n")
                break
            elif(studentsRollNo[m2]==val):
                print("Roll No. {} is found at index {} ".format(val,m2))
                print("Roll No. {} is member of the club.".format(val),"\n\n")
                break
            elif(studentsRollNo[m1]<val):
                firstIndex=m1+1
            elif(studentsRollNo[m2]>val):
                lastIndex=m2-1
    else:
        print("Roll No. {} Not Found!!!".format(val))
        print("Roll No. {} is Not member of the club.".format(val),"\n\n")

def Recursive_Ternary_Search(studentsRollNo,FirstIndex,LastIndex,value):
    if(value==studentsRollNo[LastIndex]):
        print("Roll No.{} is found at index {} ".format(value,LastIndex))
        print("Roll No. {} is member of the club.".format(value),"\n\n")
    elif(value in studentsRollNo):
        while(FirstIndex<=LastIndex):
            p1=int((FirstIndex+LastIndex)/3)
            p2=int(p1+p1)
            if(studentsRollNo[p1]==value):
                print("Roll No. {} is found at index {} ".format(value,p1))
                print("Roll No. {} is member of the club.".format(value),"\n\n")
                break
            elif(studentsRollNo[p2]==value):
                print("Roll No. {} is found at index {} ".format(value,p2))
                print("Roll No. {} is member of the club.".format(value),"\n\n")
                break
            elif(studentsRollNo[p1]<value):
                return Recursive_Ternary_Search(studentsRollNo,p1+1,LastIndex,value)
            elif(studentsRollNo[p2]>value):
                return Recursive_Ternary_Search(studentsRollNo,FirstIndex,p2-1,value)
    else:
        print("Roll No. {} Not Found!!!".format(value))
        print("Roll No. {} is Not member of the club.".format(value),"\n\n")

# Main Program
if __name__=="__main__":
    studentsRollNo=[]
    while(True):
        print("-----------------Menu--------------------\n1)Accept Students Roll No.\n2)Display Roll No.\n3)Perform Non-Recursive Ternary Search\n4)Perform Recursive Ternary Search\n5)Exit")
        choice=int(input("Enter Your Choice (from 1 to 5): "))
        if(choice==1):
            Accept_Students_Roll_No(studentsRollNo)
            sortingFunction(studentsRollNo)
        elif(choice==2):
            displayStudentsRollNo(studentsRollNo)
        elif(choice==3):
            Non_Recursive_Ternary_Search(studentsRollNo)
        elif(choice==4):
            FirstIndex=0
            LastIndex=(len(studentsRollNo)-1)
            value=int(input("Enter the Roll No. to be search: "))
            Recursive_Ternary_Search(studentsRollNo,FirstIndex,LastIndex,value)
        elif(choice==5):
            print("Thank You for using this program....")
            break
        else:
            print("Enter the valid choice....\n\n")
            
            
 -----------------------------------OUTPUT---------------------------------------------

PS C:\Users\Kunal\Desktop\DSL_LAB> python -u "c:\Users\Kunal\Desktop\DSL_LAB\DSL_ASS_13.py"
  
-----------------Menu--------------------
1)Accept Students Roll No.
2)Display Roll No.
3)Perform Non-Recursive Ternary Search
4)Perform Recursive Ternary Search
5)Exit
Enter Your Choice (from 1 to 5): 1
Enter the Number of Students: 6
Enter the Roll No. :45
Enter the Roll No. :74
Enter the Roll No. :85
Enter the Roll No. :65
Enter the Roll No. :12
Enter the Roll No. :63
Sorting is Done!!! 


-----------------Menu--------------------
1)Accept Students Roll No.
2)Display Roll No.
3)Perform Non-Recursive Ternary Search
4)Perform Recursive Ternary Search
5)Exit
Enter Your Choice (from 1 to 5): 2
12
45
63
65
74
85

-----------------Menu--------------------
1)Accept Students Roll No.
2)Display Roll No.
3)Perform Non-Recursive Ternary Search
4)Perform Recursive Ternary Search
5)Exit
Enter Your Choice (from 1 to 5): 3
Enter the Roll No. to be search: 74
Roll No. 74 is found at index 4 
Roll No. 74 is member of the club.


-----------------Menu--------------------
1)Accept Students Roll No.
2)Display Roll No.
3)Perform Non-Recursive Ternary Search
4)Perform Recursive Ternary Search
5)Exit
Enter Your Choice (from 1 to 5): 4
Enter the Roll No. to be search: 63
Roll No. 63 is found at index 2 
Roll No. 63 is member of the club.


-----------------Menu--------------------
1)Accept Students Roll No.
2)Display Roll No.
3)Perform Non-Recursive Ternary Search
4)Perform Recursive Ternary Search
5)Exit
Enter Your Choice (from 1 to 5): 5
Thank You for using this program....



--------------------------END------------------------------------
