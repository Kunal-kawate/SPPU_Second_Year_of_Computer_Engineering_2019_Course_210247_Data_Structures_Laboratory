'''
Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

Note: Please Enter the capital A for absent students.
'''
def absentStudents(marksList):
    absentCount=0
    for m in marksList:
        if(m=='A'):
            absentCount=absentCount+1
    print("Number of Absent Students",absentCount,"\n\n")

def averageScore(marksList):
    add=0
    for j in marksList:
        if(j!='A'):
         add=add+j
    print("The average score of class is",add/len(marksList),"\n\n")

def Highest_Lowest_Score(marksList):
    for k in range(0,len(marksList)):
        if(marksList[k]!='A'):
            for l in range(k,len(marksList)):
                if(marksList[l]!='A'):
                    if(marksList[k]>marksList[l]):
                        temp=marksList[k]
                        marksList[k]=marksList[l]
                        marksList[l]=temp
    
    print("Highest Score is",marksList[-1])
    print("Lowest Score is",marksList[0],"\n\n")

def highestFrequency(marksList):
    highestFrequencyNumber=0
    Frequency=0
    for n in range(0,len(marksList)):
        count=0
        for o in range(0,len(marksList)):
            if(marksList[n]==marksList[o]):
                count=count+1
        if(count>Frequency):
            Frequency=count
            highestFrequencyNumber=marksList[n]
    if(Frequency==1):
        print("No Numbers for Frequency.","\n\n")
    else:
        print(highestFrequencyNumber,"with Frequency",Frequency,"\n\n")


# Main Program
if __name__ == "__main__":
    marksList = []
    n = int(input("Enter the Number of Students: "))
    print("Note: Please Enter the capital A for Absent Students.\n\n")

    for i in range(0, n):
        FDS_marks = input("Enter the Marks (Roll No.{}): ".format(i+1))
        if (FDS_marks == 'A'):
            marksList.append(FDS_marks)
        else:
            FDS_marks = int(FDS_marks)
            marksList.append(FDS_marks)

    while (True):
        print("---------------Menu---------------:\n1)The average score of class\n2)Highest score and lowest score of class\n3)Number of Absent Students\n4)Marks with Highest Frequency\n5)Exit")
        choice = input("Enter Your Choice: ")

        if (choice == '1'):
            averageScore(marksList)
        elif(choice=='2'):
            Highest_Lowest_Score(marksList)
        elif(choice=='3'):
            absentStudents(marksList)
        elif(choice=='4'):
            highestFrequency(marksList)
        elif(choice=='5'):
            print("Thank You for using this Program..........")
            break
        else:
            print("Enter the Valid Choice......")
'''
---------------------------OUTPUT----------------------------------

                Enter the Number of Students: 5
                Note: Please Enter the capital A for absent students.

                Enter the Marks (Roll No.1): 12
                Enter the Marks (Roll No.2): 12
                Enter the Marks (Roll No.3): A
                Enter the Marks (Roll No.4): 56
                Enter the Marks (Roll No.5): 99
                ---------------Menu---------------:
                1)The average score of class
                2)Highest score and lowest score of class
                3)Number of Absent Students
                4)Marks with Highest Frequency
                5)Exit
                Enter Your Choice: 1
                The average score of class is 35.8 


                ---------------Menu---------------:
                1)The average score of class
                2)Highest score and lowest score of class
                3)Number of Absent Students
                4)Marks with Highest Frequency
                5)Exit
                Enter Your Choice: 2
                Highest Score is 99
                Lowest Score is 12 


                ---------------Menu---------------:
                1)The average score of class
                2)Highest score and lowest score of class
                3)Number of Absent Students
                4)Marks with Highest Frequency
                5)Exit
                Enter Your Choice: 3
                Number of Absent Students 1 


                ---------------Menu---------------:
                1)The average score of class
                2)Highest score and lowest score of class
                3)Number of Absent Students
                4)Marks with Highest Frequency
                5)Exit
                Enter Your Choice: 4
                12 with Frequency 2 


                ---------------Menu---------------:
                1)The average score of class
                2)Highest score and lowest score of class
                3)Number of Absent Students
                4)Marks with Highest Frequency
                5)Exit
                Enter Your Choice: 5
                Thank You for using this Program..........
'''
