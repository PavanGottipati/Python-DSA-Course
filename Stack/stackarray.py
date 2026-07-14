class StackArray:
    def __init__(self,size):
        self.size=size
        self.stack_arr=[0]* self.size
        self.top=-1

    # O(1) - Linear Time Complexity
    def push(self, ele):
        if self.top==self.size-1:
            print('Stack Overflow')
        else:
            self.top+=1
            self.stack_arr[self.top]=ele
            print('Push')
    
    # O(1) - Linear Time Complexity
    def pop(self):
        if self.top==-1:
            print('Stack Underflow')
        else:
            pop_ele=self.stack_arr[self.top]
            self.top-=1
            print('Pop ',pop_ele)
    
    # O(1) - Linear Time Complexity
    def peek(self):
        if self.top==-1:
            print('Stack is Empty!')
        else:
            print('Peek element ',self.stack_arr[self.top])

    # O(n) - Time Complexity
    def print_stack(self):
        if self.top==-1:
            print('Stack is Empty!')
        else:
            print('Stack size is ',self.top+1)
            for i in range(0,self.top+1):
                print(self.stack_arr[i],end=' ')
            print()

if __name__=="__main__":
    size=int(input('Enter size of stack : '))
    sta=StackArray(size)
    print('Menu:\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Exit')

    while True:
        ch=int(input('Enter Choice: '))
        if ch==1:
            value=int(input("Enter value to Push: "))
            sta.push(value)

        elif ch==2:
            sta.pop()

        elif ch==3:
            sta.peek()

        elif ch==4:
            sta.print_stack()

        elif ch==5:
            break
        else:
            print("Invalid Option!")