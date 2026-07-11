# Single Linked List Implementation
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    # O(n) - Linear time complexity
    def __repr__(self):
        if self.head is None:
            return "[]"
        last = self.head
        elements = []
        while last:
            elements.append(str(last.value))
            last = last.next
        return "[" + ", ".join(elements) + "]"

    # O(n) - Linear time complexity
    def __contains__(self, value):
        last=self.head
        while last:
            if last.value == value:
                return True
            last=last.next
        return False
    
    # O(n) - Linear time complexity
    def __len__(self):
        last=self.head
        counter=0
        while last:
            counter=counter+1
            last=last.next
        return counter
    
    # O(n) time complexity
    def append(self, value):
        if self.head is None:
           new_node=Node(value)
           self.head=new_node
        else:
            last=self.head
            while last.next:
                last=last.next
            last.next=Node(value)

    # O(1) constant time complexity
    def prepend(self, value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    # O(n) - Linear time complexity
    def insert(self, value, index):
        if index==0:
            self.prepend(value)
        else:
            if self.head==None:
                print("Index out of range")
                return
            else:
                last=self.head
                for i in range(index-1):
                    
                    if last.next==None:
                        print("Index out of range")
                        return
                    last=last.next
                new_node=Node(value)
                new_node.next=last.next
                last.next=new_node
    
    # O(n) - Liner time complexity
    def delete(self, value):
        if self.head is None:
            print("Empty Linked List")
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        last=self.head
        while last.next:
            if last.next.value==value:
                last.next=last.next.next
                return
            last=last.next
        print("Value not found in the list")

    # O(n) - linear time    
    def pop(self, index):
        if self.head is None:
            print("Empty Linked List")
            return
        # Case 1: Pop the head node (index 0)
        if index == 0:
            self.head = self.head.next
            return

        # Case 2: Pop a node further down the list
        last = self.head
        for i in range(index - 1):
            if last is None or last.next is None:
                print("Index out of bounds!")
                return
            last = last.next

        if last.next is None:
                print("Index out of bounds!")
                return
        else:
                last.next=last.next.next
    
    # O(n) - linear time    
    def get_element(self, index):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            last=self.head
            for i in range(index):
                if last.next==None:
                    print("Index out of bounds!")
                    return
                last=last.next
            return last.value

    # O(n) - linear time        
    def print_list(self):
        if self.head is None:
            print("Empty Linked List")
            return
        else:
            last=self.head
            while last:
                print(last.value)
                last=last.next


if __name__=="__main__":
    ll=LinkedList()
    print('Menu:\n1. Represent\n2. Contains\n3. Length\n4. Append\n5. Prepend\n6. Insert\n7. Delete\n8. Pop\n9. Get Element\n10. Show\n11. Exit')

    while True:
        ch=int(input('Enter Choice: '))
        if ch==1:
            print(ll.__repr__())
        elif ch==2:
            value=int(input("Enter value to search: "))
            result=ll.__contains__(value)
            print(result)
        elif ch==3:
            length=ll.__len__()
            print(length)
        elif ch==4:
            value=int(input("Enter value to Append: "))
            ll.append(value)
        elif ch==5:
            value=int(input("Enter value to Prepend: "))
            ll.prepend(value)
        elif ch==6:
            value=int(input("Enter value to Insert: "))
            index=int(input("Enter Index to Insert: "))
            ll.insert(value, index)
        elif ch==7:
            value=int(input("Enter value to Delete: "))
            ll.delete(value)
        elif ch==8:
            index=int(input("Enter Index to Pop: "))
            ll.pop(index)
        elif ch==9:
            index=int(input("Enter Index to Get: "))
            result=ll.get_element(index)
            print(result)
        elif ch==10:
            ll.print_list()
        elif ch==11:
            break
        else:
            print("Invalid option!")