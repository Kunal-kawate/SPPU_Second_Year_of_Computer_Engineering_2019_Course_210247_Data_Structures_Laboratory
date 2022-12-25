/*
In any language program mostly syntax error occurs due to unbalancing delimiter such as
(),{},[]. Write C++ program using stack to check whether given expression is well
parenthesized or not.
*/

#include <iostream>
using namespace std;
#define SIZE 50
char stack[SIZE];
int top = -1;

int IsFull()
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


int IsEmpty()
{
    if (top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}


void pop(string userInput){
    top=top-1;
}


void decision(void){
        if(IsEmpty()){
            cout<<"\nExpression is Valid or well Parenthesized....\n"<<endl;
        }else{
            cout<<"\nExpression is NOT Valid or NOT well Parenthesized....\n"<<endl;
        }
}


void push(string userInput)
{
    if (IsFull())
    {
        cout <<"Stack is Full!!"<< endl;
    }
    else
    {
        for (int i = 0; i < userInput.size(); i++)
        {
            if ((userInput[i] == '(') || (userInput[i] == '{') || (userInput[i] == '['))
            {
                if ((userInput[i] == '('))
                {
                    top++;
                    stack[top] = ')';
                }
                else if ((userInput[i] == '{'))
                {
                    top++;
                    stack[top] = '}';
                }
                else if ((userInput[i] == '['))
                {
                    top++;
                    stack[top] = ']';
                }
            }
            else if((userInput[i] == ')') || (userInput[i] == '}') || (userInput[i] == ']')){
                if(userInput[i]==stack[top]){
                    pop(userInput);
                }
                else{
                    break;
                }
            }
        }
        decision();
    }
}

int main()
{
    string userInput;
    cout << "\nEnter Expression to check whether it is well Parenthesized or Not: ";
    getline(cin, userInput);
    push(userInput);
    return 0;
}
