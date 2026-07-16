class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtBeg(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end="")
            if temp.next is not None:
                print(" ", end="")
            temp = temp.next
        print()
ll = LinkedList()
choice = 1
while choice != 0:
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            data = int(input("Enter data: "))
            ll.InsertAtBeg(data)
        case 2:
            ll.display()
        