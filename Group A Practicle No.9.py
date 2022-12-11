'''
Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
'''

def display_matrix(X):
    for i in X:
        print(i)
    print("\n")

def transpose_matrix(matrix_X):
    transpose_matrix_output=[]
    for i in range(0,len(matrix_X)):
        transpose_matrix_row=[]
        for j in range(0,len(matrix_X[0])):
            transpose_matrix_row.append(matrix_X[j][i])
        transpose_matrix_output.append(transpose_matrix_row)
    return transpose_matrix_output

def matrix(matrix_rows,matrix_cols):
    matrix_output=[]
    for i in range(0,matrix_rows):
        matrix_row=[]
        for j in range(0,matrix_cols):
            num=int(input("Enter the value: "))
            matrix_row.append(num)
        matrix_output.append(matrix_row)
    return matrix_output

def addition(matrix_A,matrix_B):
    addition_matrix_output=[]
    for i in range(0,len(matrix_A)):
        addition_matrix_row=[]
        for j in range(0,len(matrix_A[0])):
            addition_matrix_row.append(matrix_A[i][j]+matrix_B[i][j])
        addition_matrix_output.append(addition_matrix_row)
    return addition_matrix_output

def subtraction(matrix_A,matrix_B):
    subtraction_matrix_output=[]
    for i in range(0,len(matrix_A)):
        subtraction_matrix_row=[]
        for j in range(0,len(matrix_A[0])):
            subtraction_matrix_row.append(matrix_A[i][j]-matrix_B[i][j])
        subtraction_matrix_output.append(subtraction_matrix_row)
    return subtraction_matrix_output

def multiplication(matrix_A,matrix_B):
    multiplication_matrix_output=[]
    for i in range(0,len(matrix_A)):
        multiplication_matrix_row=[]
        for j in range(0,len(matrix_A[0])):
            multiplication_matrix_row.append(matrix_A[i][j]*matrix_B[j][i])
        multiplication_matrix_output.append(multiplication_matrix_row)
    return multiplication_matrix_output

# Main Program
if __name__=="__main__":
    matrix_rows=int(input("Enter the rows of matrix: "))
    matrix_cols=int(input("Enter the cols of matrix: "))
    print("\nMatrix-A")
    matrix_A=matrix(matrix_rows,matrix_cols)
    display_matrix(matrix_A)
    print("Matrix-B")
    matrix_B=matrix(matrix_rows,matrix_cols)
    display_matrix(matrix_B)

    while(True):
        print("---------------------Menu---------------------\n1)Perform Addition of Matrix A and B\n2)Perform Subtraction of Matrix A and B\n3)Multiplication of Matrix A and B\n4)Exit")
        choice=int(input("Enter your choice (From 1 to 4): "))
        print("\n")
        if(choice==1):
            addition_matrix=addition(matrix_A,matrix_B)
            print("Addition of Matrix A and Matrix B is-")
            display_matrix(addition_matrix)
            addition_matrix_transpose=transpose_matrix(addition_matrix)
            print("Transpose of Addition Matrix-")
            display_matrix(addition_matrix_transpose)
        elif(choice==2):
            subtraction_matrix=subtraction(matrix_A,matrix_B)
            print("Subtraction of Matrix A and Matrix B is-")
            display_matrix(subtraction_matrix)
            subtraction_matrix_transpose=transpose_matrix(subtraction_matrix)
            print("Transpose of subtraction Matrix-")
            display_matrix(subtraction_matrix_transpose)
        elif(choice==3):
            multiplication_matrix=multiplication(matrix_A,matrix_B)
            print("Multiplication of Matrix A and Matrix B is-")
            display_matrix(multiplication_matrix)
            print("Transpose of Multiplication Matrix-")
            multiplication_matrix_transpose=transpose_matrix(multiplication_matrix)
            display_matrix(multiplication_matrix_transpose)
        elif(choice==4):
            print("Thank You For Using This Program.....")
            break
        else:
            print("Please Enter Valid Choice...")
     
------------------------------------OUTPUT-------------------------------------------
  
Enter the rows of matrix: 3
Enter the cols of matrix: 3

Matrix-A
Enter the value: 4
Enter the value: 5
Enter the value: 7
Enter the value: 8
Enter the value: 4
Enter the value: 6
Enter the value: 3
Enter the value: 1
Enter the value: 5
[4, 5, 7]
[8, 4, 6]
[3, 1, 5]


Matrix-B
Enter the value: 7
Enter the value: 9
Enter the value: 5
Enter the value: 4
Enter the value: 2
Enter the value: 1
Enter the value: 6 
Enter the value: 7
Enter the value: 6
[7, 9, 5]
[4, 2, 1]
[6, 7, 6]


---------------------Menu---------------------
1)Perform Addition of Matrix A and B
2)Perform Subtraction of Matrix A and B
3)Multiplication of Matrix A and B
4)Exit
Enter your choice (From 1 to 4): 1


Addition of Matrix A and Matrix B is-
[11, 14, 12]
[12, 6, 7]
[9, 8, 11]


Transpose of Addition Matrix-
[11, 12, 9]
[14, 6, 8]
[12, 7, 11]


---------------------Menu---------------------
1)Perform Addition of Matrix A and B
2)Perform Subtraction of Matrix A and B
3)Multiplication of Matrix A and B
4)Exit
Enter your choice (From 1 to 4): 2


Subtraction of Matrix A and Matrix B is-
[-3, -4, 2]
[4, 2, 5]
[-3, -6, -1]


Transpose of subtraction Matrix-
[-3, 4, -3]
[-4, 2, -6]
[2, 5, -1]


---------------------Menu---------------------
1)Perform Addition of Matrix A and B
2)Perform Subtraction of Matrix A and B
3)Multiplication of Matrix A and B
4)Exit
Enter your choice (From 1 to 4): 3


Multiplication of Matrix A and Matrix B is-
[28, 20, 42]
[72, 8, 42]
[15, 1, 30]


Transpose of Multiplication Matrix-
[28, 72, 15]
[20, 8, 1]
[42, 42, 30]


---------------------Menu---------------------
1)Perform Addition of Matrix A and B
2)Perform Subtraction of Matrix A and B
3)Multiplication of Matrix A and B
4)Exit
Enter your choice (From 1 to 4): 4

Thank You For Using This Program.....
