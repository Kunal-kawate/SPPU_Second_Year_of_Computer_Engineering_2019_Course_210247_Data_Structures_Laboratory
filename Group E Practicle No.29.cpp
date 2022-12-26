/*
Queues are frequently used in computer programming, and a typical example is the
creation of a job queue by an operating system. If the operating system does not use
priorities, then the jobs are processed in the order they enter the system. Write C++
program for simulating job queue. Write functions to add job and delete job from queue.
*/

#include <iostream>
using namespace std;
# define SIZE 50
int queue[SIZE];
int front=-1;
int back=-1;

void push(int x){
    if(back==SIZE-1){
        cout<<"Queue is overflow!!!"<<endl;
    }else{
        if(front==-1){
            front++;
        }
        back++;
        queue[back]=x;
        cout<<queue[back]<<" is push on the queue.\n"<<endl;
    }
}

void pop(void){
    if(front==-1 || front>back){
        cout<<"Queue is underflow!!!!"<<endl;
    }else{
        cout<<"\n"<<queue[front]<<" is pop from the queue."<<endl;
        front++;
    }
}

void display(void){
    cout<<"Queue elements are: "<<endl;
    for(int i=front;i<=back;i++){
        cout<<queue[i]<<endl;
    }
}

int main(){
    int choice;
    int job;
    bool condition=true;
    while (condition)
    {
        cout<<"\n--------------MENU---------------\n1)Add Job.\n2)Delete Job.\n3)Display Jobs.\n4)Exit"<<endl;
        cout<<"Enter your choice(from 1 to 4): ";
        cin>>choice;

        switch(choice){
            case 1:
                cout<<"\nEnter Job:";
                cin>>job;
                push(job);
                break;
            
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                condition=false;
                cout<<"Thank You for using this Program....\n"<<endl;
                break;
            default:
            cout<<"Plaese Enter Valid Choice!!!"<<endl;
        }   
    }
    return 0;
}
