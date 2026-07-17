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

    def InsertAtEnd(self,data):
        curr=self.head
        newnode=Node(data)
        if curr==None:
            self.head=newnode
        else:
            while curr.next != None:
                curr=curr.next
            curr.next=newnode
            newnode.next=None
    def InsertAtpos(self,data,pos):
        curr=self.head
        newNode=Node(data)
        if(pos==1):
            self.InsertAtBeg(data)
        else:
            if(self.head==None):
                print("list is empty")
            else:
                temp=self.head
                i=1
                while i<pos-1:
                    if temp!=None:
                        temp=temp.next
                        i+=1
                    else:
                        print("invalid pos")
                        return
                newNode.next=temp.next
                temp.next=newNode
    def DeleteAtBeg(self):
        if self.head==0:
            print("empty!!")
        else:
            self.head=self.head.next
        print()

    def DeleteAtEnd(self):
        if self.head==None:
            print("Empty list")
            return
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.next
            curr.next=None
    def DeleteAtGivenPos(self):
        if(pos==1):
            self.DeleteAtBeg()
        else:
            if(self.head==None):
                print("list is empty!!")
            else:
                temp=self.head
                i=1
                while i<pos-1:
                    if temp!=None:
                        temp=temp.next
                        i+=1
                    else:
                        print("invalid position!!")
                        return
                    temp.next=temp.next.next
                        

print("1) Insert at beginning")
print("2) Insert at end")
print("3) display")
print("4) Insert at given position")
print("5) Delete at Beginning")
print("6) Delete at End")
print("7) Delete at Given Position")

ll = LinkedList()
choice = 1
while choice != 0:
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            data = int(input("Enter data: "))
            ll.InsertAtBeg(data)
        case 2:
            data = int(input("Enter data: "))
            ll.InsertAtEnd(data)
        case 3: 
            ll.display()
        case 4:
            data = int(input("Enter data: "))
            pos= int(input("Enter position: "))
            ll.InsertAtpos(data,pos)
        case 5:
            ll.DeleteAtBeg()
        case 6:
            ll.DeleteAtEnd()
        case 7: 
            ll.DeleteAtGivenPos()
            data = int(input("Enter data: "))
print()