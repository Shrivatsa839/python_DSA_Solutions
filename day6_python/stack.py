class stack1:
    def _init_(self,size=5,top=-1):
        self.size=size
        self.top=top
        self.stack=[0]*size
        
    def overflow(self):
        return self.top==self.size-1

    def underflow(self):
        return self.top==-1
    
    def pop(self):
        if (self.underflow()):
            print("Underflow")
        else:
            self.stack[self.top]=0
            self.top-=1
            
    def push(self,data):
        if (self.overflow()):
            print("Overflow")
        else:
            self.top+=1
            self.stack[self.top]=data
    
    def display(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
        
s=stack1()

choice=1
while choice!=0:

    print("1 for push , 2 for pop , 3 for display")
    choice=int(input("Enter choice: "))
    match choice:
        case 1:
            data=int(input("Data? :"))
            s.push(data)
        case 2:
            s.pop()
        case 3:
            s.display() 