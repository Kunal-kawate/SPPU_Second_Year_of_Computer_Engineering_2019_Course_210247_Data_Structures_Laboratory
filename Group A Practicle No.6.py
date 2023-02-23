'''
It is decided that weekly greetings are to be furnished to wish the students having their
birthdays in that week. The consolidated sorted list with desired categorical information
is to be provided to the authority. Write a python program to store students PRNs with
date and month of birth. Let List_A and List_B be the two list for two SE Computer
divisions. Lists are sorted on date and month. Merge these two lists into third list
“List_SE_Comp_DOB” resulting in sorted information about Date of Birth of SE Computer
students
'''

from datetime import datetime

if __name__=="__main__":
    List_A=[]
    print("\nList_A:")
    n1=int(input("\nEnter the number of students:"))
    for i in range(n1):
        tempDict={}
        prn=input("\nEnter your PRN no. : ")
        dob=input("\nEnter your date of birth(DD-MM): ")
        tempDict['PRN']=prn
        tempDict['DOB']=dob
        List_A.append(tempDict)
    List_A.sort(key = lambda x: datetime.strptime(x['DOB'],'%d-%m'))
    print("\nSorted Data:")
    for item in List_A:
        print(item)

    List_B=[]
    print("\nList_B:")
    n2=int(input("\nEnter the number of students:"))
    for j in range(n2):
        tempDict={}
        prn=input("\nEnter your PRN no. : ")
        dob=input("\nEnter your date of birth(DD-MM): ")
        tempDict['PRN']=prn
        tempDict['DOB']=dob
        List_B.append(tempDict)
    List_B.sort(key = lambda x: datetime.strptime(x['DOB'],'%d-%m'))
    print("\nSorted Data:")
    for item in List_B:
        print(item)

    print("\nList_SE_Comp_DOB: ")
    List_SE_Comp_DOB=List_A+List_B
    List_SE_Comp_DOB.sort(key = lambda x: datetime.strptime(x['DOB'],'%d-%m'))
    print("Sorted Data:")
    for item in List_SE_Comp_DOB:
        print(item)
        
