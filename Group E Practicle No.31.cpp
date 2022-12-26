/*
A double-ended queue (deque) is a linear list in which additions and deletions may be
made at either end. Obtain a data representation mapping a deque into a one-
dimensional array. Write C++ program to simulate deque with functions to add and
delete elements from either end of the deque.
*/

#include <iostream>
using namespace std;
# define SIZE 50
int arr[SIZE]={4,5,6};
int front=-1;
int back=-1;
int size=-1;

void insert_at_beg(int num){
    if(back==SIZE-1){
        cout<<"\nDouble Ended Queue is Full!!!!!!\n"<<endl;
    }else{
        if(front==-1){
            front++;
            back++;
            size++;
            arr[front]=num;
            cout<<"\nElement "<<num<<" is Successfully Inserted at Beg!!\n"<<endl;
        }else{
            for(int i=back;i>=front;i--){
                arr[i+1]=arr[i];
            }
            size++;
            back++;
            arr[front]=num;
            cout<<"\nElement "<<num<<" is Successfully Inserted at Beg!!\n"<<endl;
        }
    }
}

void display(void){
    if(front==-1 || front>back){
        cout<<"\nQueue is Empty!!\n"<<endl;
    }else{
        cout<<"\nQueue Elements are-"<<endl;
        for(int j=front;j<=size;j++){
            cout<<arr[j]<<endl;
        }
    }
}

void insert_at_end(int num){
    if(back==SIZE-1){
        cout<<"\nDouble Ended Queue is Full!!!\n"<<endl;
    }else{
         if(back==-1){
            front++;
            back++;
            size++;
            arr[back]=num;
            cout<<"\nElement "<<num<<" is Successfully Inserted at End!!\n"<<endl;
        }
        else{
            back++;
            size++;
            arr[back]=num;
            cout<<"\nElement "<<num<<" is Successfully Inserted at End!!\n"<<endl;
        }
    }
}

void deletion_from_front(void){
    if(front==-1 || front>back){
        cout<<"\nDouble Ended Queue is Empty!!\n"<<endl;
    }else{
        cout<<"\nElement "<<arr[front]<<" is deleted!!\n"<<endl;
        front++;
    }
}

void deletion_from_back(void){
    if(front==-1 || front>back){
        cout<<"\nDouble Ended Queue is Empty!!\n"<<endl;
    }else{
        cout<<"\nElement "<<arr[back]<<" is deleted!!\n"<<endl;
        back--;
        size--;
    }
}

int main(){
    int choice;
    int num;
    bool condition=true;
    while(condition){
        cout<<"\n---------------MENU------------------\n1)Insert at Beg\n2)Insert at End\n3)Deletion form front\n4)Deletion form back\n5)Display\n6)Exit"<<endl;
        cout<<"Enter your choice(From 1 to 6): ";
        cin>>choice;
        switch(choice){
            case 1:
                cout<<"Enter the value: ";
                cin>>num;
                insert_at_beg(num);
                break;
            case 2:
                cout<<"Enter the value: ";
                cin>>num;
                insert_at_end(num);
                break;
            case 3:
                deletion_from_front();
                break;
            case 4:
                deletion_from_back();
                break;
            case 5:
                display();
                break;
            case 6:
                condition=false;
                cout<<"\nThank You for using this program.....\n"<<endl;
                break;
            default:
                cout<<"\nPlease enter Valid choice!!\n"<<endl;
        }
    }
    return 0;
}
