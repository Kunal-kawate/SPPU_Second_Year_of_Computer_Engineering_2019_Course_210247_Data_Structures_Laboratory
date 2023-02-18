'''
Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following: D
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500
'''

if __name__=="__main__":

    condition=True
    balance=0

    transactionList=[]
    while(condition):
        transaction=input("\nEnter the transaction log: ")
        if(transaction=='x'):
            condition=False
            print("\nThank You for using this program!!\n")
        else:
            transactionSplit=transaction.split()
            if(transactionSplit[0]=='D' or transactionSplit[0]=='W' ):
                if(transactionSplit[0]=='D'):
                    balance=balance+int(transactionSplit[1])
                    transactionList.append(transactionSplit)
                    print("\nTransaction List : ",transactionList)
                    print("\nBalance: ",balance)
                elif( transactionSplit[0]=='W' ):
                    if(balance>=int(transactionSplit[1])):
                        balance=balance-int(transactionSplit[1])
                        transactionList.append(transactionSplit)
                        print("\nTransaction List : ",transactionList)
                        print("\nBalance: ",balance)
                    else:
                        print("\nWithdraw not possible because balance is less!!")
                        print("\nTransaction List : ",transactionList)
                        print("\nBalance: ",balance)
            else:
                print("\nPlease Enter the Valid Log!!!")
