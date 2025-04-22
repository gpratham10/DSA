class Stack:
    def create_stack(self):
        self.s=[]
    def push(self,e):
        self.s.append(e)
        print("pushed")
    def pop(self):#remove and return
        return self.s.pop()
        #by default removes last
    def peek(self):#only return
        return self.s[-1]
        #by default removes last
    def is_empty(self):#true if len 0 else false
        return len(self.s)==0
    def print_stack(self):
       for item in self.s[::-1]:
        print(item)


obj=Stack()
obj.create_stack()
while True:
    print("\nStack Menu")
    print("------------")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Print")
    print("0.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        obj.push(int(input("Enter element:")))
    elif ch==2:
        if obj.is_empty()!=True:
            print("Poped:",obj.pop())
        else:
            print("Empty stack")
    elif ch==3:
        if obj.is_empty()!=True:
            print("Peek is:",obj.peek())
        else:
            print("Empty stack")
    elif ch==4:
        if obj.is_empty()!=True:
            obj.print_stack()
        else:
            print("Empty stack")
    elif ch==0:
        print("Exiting....")
        break
    else:
        print("Wrong input")
