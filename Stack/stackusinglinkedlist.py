class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class StackSingleLinkedList:
    def __init__(self):
        self.top=None
    
    def push(self, value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        print('Pushed => ', value)

    def pop(self):
        if self.top is None:
            print('Stack Underflow!')
        else:
            pop_ele=self.top.value
            self.top=self.top.next
            print('Popped => ',pop_ele)

    def peek(self):
        if self.top is None:
            print('Stack Empty!')
        else:
            print('Peek element ',self.top.value)
    
    def print_stack(self):
        if self.top is None:
            print('Stack Empty!')
        else:
            count=0
            current=self.top
            stack_elements=[]
            while current:
                stack_elements.append(str(current.value))
                current=current.next
                count+=1
            print('The Size Of Stack is ', count)
            print(" -> ".join(stack_elements))

if __name__=="__main__":
    
    sta=StackSingleLinkedList()
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
            print("Invalid option!")