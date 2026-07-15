class CircularQueueArray:
    def __init__(self,n):
        self.n=n
        self.front=-1
        self.rear=-1
        self.arr=[None]*n
        self.size=0
    
    #O(1) - Linear Time Complexity
    def enqueue(self):
        if ((self.rear+1)%self.n==self.front):
            print('Queue Overflow!')
            return
        val=int(input('Enter value : '))
        self.rear=(self.rear+1)%self.n
        self.arr[self.rear]=val
        if(self.front==-1):
            self.front=0
        self.size+=1
        print('Enqueue => ',val)
    
    #O(1) - Linear Time Complexity
    def dequeue(self):
        if(self.front==-1):
            print('Queue Underflow!')
            return
        dequeue_ele=self.arr[self.front]
        if(self.front==self.rear):
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.n
        self.size-=1
        print('Dequeue => ',dequeue_ele)

    #O(n) - Time Complexity
    def display(self):
        if(self.front==-1):
            print('Queue is Empty!')
            return
        temp=self.front
        print('Size of Queue => ',self.size)
        print('Elements in the Circular Queue are: ', end='')
        while True:
            print(self.arr[temp], end=' ')
            if temp==self.rear:
                break
            temp=(temp+1)%self.n
        print()

if __name__=="__main__":
    size=int(input('Enter size of Queue : '))
    queue=CircularQueueArray(size)
    print('Menu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit')

    while True:
        ch=int(input('Enter Choice: '))
        if ch==1:
            queue.enqueue()

        elif ch==2:
            queue.dequeue()

        elif ch==3:
            queue.display()

        elif ch==4:
            break
        else:
            print("Invalid option!")