class Node:
    def __init__(self, value): 
        self.value=value
        self.next=None
        

class CircularLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
    
    #O(n) - linear time complexity
    def append(self, value):
        if self.head is None:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
            print('Node added since Empty list')
        else:
            last=self.head.next
            while last!=self.tail:
                last=last.next

            new_node=Node(value)
            last.next=new_node
            new_node.next=self.head
            self.tail=new_node
            print('Node added to existing')
        
   #O(1) - constant time complexity
    def prepend(self, value):
        if self.head is None:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
            new_node.next=self.head
            print('Node prepended since Empty list')
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
            print('Node prepended to existing')

    #O(1) - constant time complexity
    def deleteFirst(self):
        if self.head is None:
            print('Empty List to delete first')
        else:
            if self.head==self.tail:
                self.head, self.tail=None, None
                print('Single Node deleted from first')
            else:
                self.head=self.head.next
                self.tail.next=self.head
                print('Node deleted from first')

    #O(n) - linear time complexity
    def deleteLast(self):
        if self.head is None:
            print('Empty List to delete second')
        else:
            if self.head==self.tail:
                self.head, self.tail=None, None
                print('Single Node deleted from last')
            else:
                last=self.head
                while last.next!=self.tail:
                    last=last.next
                last.next=self.head
                self.tail=last
                print('Deleted from last')

    #O(n) - linear time complexity
    def printlist(self):
        if self.head is None:
            print('Empty List to print')
        elif self.head==self.tail:
            print(self.head.value)
        else:
            last=self.head
            while last!=self.tail:
                print(last.value)
                last=last.next
            print(last.value)

if __name__=="__main__":
    cll=CircularLinkedList()
    print('Menu:\n1. Append\n2. Prepend\n3. DeleteFirst\n4. DeleteLast\n5. Print\n6. Exit')

    while True:
        ch=int(input('Enter Choice: '))
        if ch==1:
            value=int(input("Enter value to append: "))
            cll.append(value)

        elif ch==2:
            value=int(input("Enter value to prepend: "))
            result=cll.prepend(value)

        elif ch==3:
            cll.deleteFirst()

        elif ch==4:
            cll.deleteLast()

        elif ch==5:
            cll.printlist()
        elif ch==6:
            break
        else:
            print("Invalid option!")