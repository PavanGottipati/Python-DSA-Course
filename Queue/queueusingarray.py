class QueueArray:
    def __init__(self, n):
        self.n=n
        self.front=-1
        self.rear=-1
        self.size=0
        self.arr = [None] * n
    
    #O(1) - Linear Time Complexity
    def enqueue(self):
        if(self.rear==self.n-1):
            print('Queue Overflow!')
            return
        val=int(input('Enter value : '))
        self.rear+=1
        self.arr[self.rear]=val
        if self.front==-1:
            self.front=0
        self.size+=1
        print('Enqueue => ',val)
        
    #O(1) - Linear Time Complexity
    def dequeue(self):
        if(self.front==-1):
            print('Queue Overflow!')
            return
        dequeue_ele=self.arr[self.front]
        self.front=self.front+1
        self.size-=1
        if(self.front>self.rear):
            self.front=-1
            self.rear=-1
        print('Dequeue => ',dequeue_ele)
    
    #O(n) - Linear Time Complexity
    def display(self):
        if(self.front==-1):
            print('Queue is Empty!')
            return
        temp=self.front
        print('The size of Queue is ',self.size)
        queue_arr=[]
        while(temp<=self.rear):
            queue_arr.append(self.arr[temp])
            temp=temp+1
        print(queue_arr)

if __name__=="__main__":
    size=int(input('Enter size of Queue : '))
    queue=QueueArray(size)
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