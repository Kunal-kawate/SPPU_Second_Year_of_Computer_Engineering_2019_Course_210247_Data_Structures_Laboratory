'''In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do not use SET
built-in functions)'''

def universalSet(cricketList,footballList,badmintonList):
    universalList=[]
    for i in cricketList:
        universalList.append(i)
    for j in footballList:
        if(j not in universalList):
            universalList.append(j)  
    for k in badmintonList:
        if(k not in universalList):
            universalList.append(k)
    print("The Universal Set is ",universalList)
    print("The students Playing Cricket are ",cricketList)
    print("The students Playing Football are ",footballList)
    print("The students Playing Badminton are ",badmintonList,"\n")

def cricketANDbadminton(cricketList,badmintonList):
    cricketANDbadmintonList=[]
    for l in cricketList:
        if(l in badmintonList):
            cricketANDbadmintonList.append(l)
    print("List of students who play both Cricket and Badminton: ",cricketANDbadmintonList,"\n")

def either_cricket_or_badminton(cricketList,badmintonList):
    either_cricket_or_badminton_List=[]
    for m in cricketList:
        if(m not in badmintonList):
            either_cricket_or_badminton_List.append(m)
    for n in badmintonList:
        if(n not in cricketList):
            either_cricket_or_badminton_List.append(n)
    print("List of students who play either cricket or badminton but not both: ",either_cricket_or_badminton_List,"\n")

def neither_cricket_nor_badminton(cricketList,badmintonList,footballList):
    neither_cricket_nor_badminton_List=[]
    for o in footballList:
        if((o not in cricketList) and (o not in badmintonList)):
            neither_cricket_nor_badminton_List.append(o)
    print("The no. of student who play neither cricket nor badminton is: ",len(neither_cricket_nor_badminton_List))
    print("The student who play neither cricket nor badminton are: ",neither_cricket_nor_badminton_List,"\n")

def cricket_and_football_but_not_badminton(cricketList,badmintonList,footballList):
    cricket_and_football_but_not_badminton_List=[]
    for p in cricketList:
        cricket_and_football_but_not_badminton_List.append(p)
    
    for q in footballList:
        if(q not in cricket_and_football_but_not_badminton_List):
            cricket_and_football_but_not_badminton_List.append(q)
    
    for r in cricket_and_football_but_not_badminton_List:
        if(r in badmintonList):
            cricket_and_football_but_not_badminton_List.remove(r)
    print("The no. of student who play cricket and football bot bot badminton is: ",len(cricket_and_football_but_not_badminton_List))
    print("The students who play cricket and football bot not badminton: ",cricket_and_football_but_not_badminton_List,"\n")

#main 
if __name__ == "__main__":
    cricketList = []
    n1 = int(input("Enter the No. of Students playing Cricket: "))
    for i in range(0, n1):
        cricketStudent = input("Enter the name of student: ")
        cricketList.append(cricketStudent)
    print("\n")

    footballList = []
    n2 = int(input("Enter the No. of Students playing Football: "))
    for i in range(0, n2):
        footballStudent = input("Enter the name of student: ")
        footballList.append(footballStudent)
    print("\n")

    badmintonList = []
    n3 = int(input("Enter the No. of Students playing Badminton: "))
    for i in range(0, n3):
        badmintonStudent = input("Enter the name of student: ")
        badmintonList.append(badmintonStudent)
    print("\n")
    #functions call
    universalSet(cricketList,footballList,badmintonList)
    cricketANDbadminton(cricketList,badmintonList)
    either_cricket_or_badminton(cricketList,badmintonList)
    neither_cricket_nor_badminton(cricketList,badmintonList,footballList)
    cricket_and_football_but_not_badminton(cricketList,badmintonList,footballList)

#----------------OUTPUT--------------------------------
'''
Enter the No. of Students playing Cricket: 3
Enter the name of student: Kunal
Enter the name of student: Aadhira
Enter the name of student: Aadi


Enter the No. of Students playing Football: 5
Enter the name of student: Nila
Enter the name of student: Shyla
Enter the name of student: Aadhira
Enter the name of student: Reva
Enter the name of student: Ishani


Enter the No. of Students playing Badminton: 4
Enter the name of student: Aadi
Enter the name of student: Kunal
Enter the name of student: Nila
Enter the name of student: Shyla


The Universal Set is  ['Kunal', 'Aadhira', 'Aadi', 'Nila', 'Shyla', 'Reva', 'Ishani']
The students Playing Cricket are  ['Kunal', 'Aadhira', 'Aadi']
The students Playing Football are  ['Nila', 'Shyla', 'Aadhira', 'Reva', 'Ishani']
The students Playing Badminton are  ['Aadi', 'Kunal', 'Nila', 'Shyla']

List of students who play both Cricket and Badminton:  ['Kunal', 'Aadi']

List of students who play either cricket or badminton but not both:  ['Aadhira', 'Nila', 'Shyla']

The no. of student who play neither cricket nor badminton is:  2
The student who play neither cricket nor badminton are:  ['Reva', 'Ishani']

The no. of student who play cricket and football bot bot badminton is:  4
The students who play cricket and football bot not badminton:  ['Aadhira', 'Nila', 'Reva', 'Ishani']
'''