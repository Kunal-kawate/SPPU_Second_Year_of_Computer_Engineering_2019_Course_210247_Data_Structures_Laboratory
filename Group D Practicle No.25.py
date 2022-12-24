/*
A palindrome is a string of character that‘s the same forward and backward. Typically,
punctuation, capitalization, and spaces are ignored. For example, “Poor Dan is in a droop”
is a palindrome, as can be seen by examining the characters “poor danisina droop” and
observing that they are the same forward and backward. One way to check for a
palindrome is to reverse the characters in the string and then compare with them the
original-in a palindrome, the sequence will be identical. Write C++ program with
functions-
a) To print original string followed by reversed string using stack
b) To check whether given string is palindrome or not
*/

#include <iostream>
using namespace std;
#define SIZE 50
char arr[SIZE];
int top = -1;

int isFull()
{
    if (top == SIZE - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isEmpty(){
    if(top==-1){
        return 0;
    }else{
        return 1;
    }
}

void reversed(string statement1,string statement2){
    while(isEmpty()){
        statement2+=arr[top];
        top=top-1;
    }
    cout<<"\nReverse String is: "<<statement2<<endl;
    if(statement1==statement2){
        cout<<"\nString is Palindrome.....\n"<<endl;
    }else{
        cout<<"\nString is NOT Palindrome.....\n"<<endl;
    }
}

void push(string userInput,string statement1,string statement2)
{
    for (int i = 0; i < userInput.size(); i++)
    {
        if(isFull()){
            cout<<"Stack is Full!!"<<endl;
        }else{
            if((int(userInput[i])>=65 && int(userInput[i])<=90)||(int(userInput[i])>=97 && int(userInput[i])<=122)){
                top++;
                cout << userInput[i] << " is Push on Stack..." << endl;
                statement1+=char(tolower(userInput[i]));
                arr[top] =char(tolower(userInput[i]));
            }
        }
    }
    reversed(statement1,statement2);
}

int main()
{
    string userInput,statement1,statement2;
    cout << "Enter String to be reversed and check it is Palindrome or Not: ";
    getline(cin, userInput);
    push(userInput,statement1,statement2);
    return 0;
}


