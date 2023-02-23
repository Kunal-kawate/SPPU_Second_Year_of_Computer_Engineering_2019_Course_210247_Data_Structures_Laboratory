'''
Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string
'''

def longestLengthWord(inputString):
    tempString=""
    for i in range(len(inputString)):
        if((ord(inputString[i])>=65 and ord(inputString[i])<=90) or (ord(inputString[i])>=96 and ord(inputString[i])<=122) or (ord(inputString[i])==32)):
            tempString=tempString+inputString[i]
    tempList=tempString.split()
    print("\nThe longest word is ",max(tempList, key=len)," and its length is ",len(max(tempList, key=len)))

def characterFrequency(inputString):
    characterFrequencyDict={}
    for item in inputString:
        count=0
        for i in range(len(inputString)):
            if(item==inputString[i]):
                count=count+1
        characterFrequencyDict[item]=count
    print("\nThe frequency of occurrence of particular character in the string: ",characterFrequencyDict)

def palindromeString(inputString):
    tempString1=""
    tempString2=""
    for i in range(len(inputString)):
        if((ord(inputString[i])>=65 and ord(inputString[i])<=90) or (ord(inputString[i])>=96 and ord(inputString[i])<=122)):
            tempString1=tempString1+inputString[i]
    j=len(tempString1)-1
    while(j>=0):
        tempString2=tempString2+tempString1[j]
        j=j-1
    if(tempString1==tempString2):
        print("\nGiven string is Palindrome....")
    else:
        print("\nGiven string is Not Palindrome....")

def indexFind(inputString):
    userWord=input("\nEnter word: ")
    if userWord in inputString:
        print("\nIndex of first appearance of substring is",inputString.find(userWord)+1)
    else:
        print("\nYour word is not prsent in string!!!")

def wordOccurrences(inputString):
    wordOccurrencesDict={}
    tempString=""
    for i in range(len(inputString)):
        if((ord(inputString[i])>=65 and ord(inputString[i])<=90) or (ord(inputString[i])>=96 and ord(inputString[i])<=122) or (ord(inputString[i])==32)):
            tempString=tempString+inputString[i]
    tempList=tempString.split()
    for item in tempList:
        count=0
        for i in range(len(tempList)):
            if(item==tempList[i]):
                count=count+1
        wordOccurrencesDict[item]=count
    print("\nThe occurrences of each word in a given string is ",wordOccurrencesDict)

if __name__=="__main__":
    inputString=input("\nEnter the string: ")
    condition=True
    while(condition):
        choice=int(input("\n------------------------------MENU----------------------------\n1)Display word with the longest length\n2)Determines the frequency of occurrence of particular character in the string\n3)Check whether given string is palindrome or not\n4)Display index of first appearance of the substring\n5)Count the occurrences of each word in a given string\n6)Exit\nEnter your choice: "))
        if(choice==1):
            longestLengthWord(inputString)
        elif(choice==2):
            characterFrequency(inputString)
        elif(choice==3):
            palindromeString(inputString)
        elif(choice==4):
            indexFind(inputString)
        elif(choice==5):
            wordOccurrences(inputString)
        elif(choice==6):
            condition=False
            print("\nThank you for using this program......\n")
        else:
            print("\nEnter Valid choice!!!!!")
