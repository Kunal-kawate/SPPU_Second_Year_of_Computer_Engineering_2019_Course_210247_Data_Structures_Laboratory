/*
Pizza parlor accepting maximum M orders. Orders are served in first come first served
basis. Order once placed cannot be cancelled. Write C++ program to simulate the system
using circular queue using array.
*/

#include <iostream>
using namespace std;
# define SIZE 5
int orders[SIZE];
int front=-1;
int back=-1;

void AcceptOrder(int count){
    if(back==-1){
        front=0;
        back=0;
        orders[back]=count;
        cout<<"\nYour order ID is - "<<count<<endl;
    }else{
        if((back+1)%SIZE==front){
            cout<<"\nCafe is Full. Please Wait!!\n"<<endl;
        }else{
            back=(back+1)%SIZE;
            orders[back]=count;
            cout<<"\nYour order ID is - "<<count<<endl; 
        }
    }
}

void ServeOrder(void){
    if(front==-1){
        cout<<"\nNo orders are remaining!!\n"<<endl;
    }else{
        cout<<"\nOrder "<<orders[front]<<" is processed!!"<<endl;
        if(front==back){
            front=-1;
            back=-1;
        }else{
            front=(front+1)%SIZE;
        }
    }
}

void display(){
    if(front==-1 ){
        cout<<"\nCafe is Empty!!\n"<<endl;
    }else{
        cout<<"\nOrders- "<<endl;
        for(int i=front;i!=back;i=(i+1)%SIZE){
            cout<<orders[i]<<endl;
        }
        cout<<orders[back]<<endl;
    }
}

int main(){
    int choice;
    int count=0;
    bool condition=true;
    while (condition)
    {
        cout<<"\n-------------------MENU--------------------\n1)Accept Order.\n2)Serve Order.\n3)Display Orders.\n4)Exit."<<endl;
        cout<<"Enter Your Choice(From 1 to 4):";
        cin>>choice;

        switch(choice){
            case 1:
                count++;
                AcceptOrder(count);
                break;
            case 2:
                ServeOrder();
                break;
            case 3:
                display();
                break;
            case 4:
                condition=false;
                cout<<"\nThank You for using this program......\n"<<endl;
                break;
            default:
                cout<<"\nEnter Valid Choice!!\n"<<endl;
        }
    }
    return 0;
}


