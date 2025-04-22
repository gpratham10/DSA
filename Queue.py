class Queue:
    def create_queue(self):
        self.q=[]
    def enqueue(self,e):
        self.q.append(e)
        print("Enqueued")
    def dequeue(self):#remove and return
        return self.q.pop(0)
    def is_empty(self):#true if len 0 else false
        return len(self.q)==0
    def print_queue(self):
       for item in self.q:
        print(item,end=" - ")
obj=Queue()
obj.create_queue()
while True:
    print("\nQueue Menu")
    print("------------")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Print")
    print("0.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        obj.enqueue(int(input("Enter element:")))
    elif ch==2:
        if obj.is_empty()!=True:
            print("Dequeued:",obj.dequeue())
        else:
            print("Empty queue")
    elif ch==3:
        if obj.is_empty()!=True:
            obj.print_queue()
        else:
            print("Empty queue")
    elif ch==0:
        print("Exiting....")
        break
    else:
        print("Wrong input")



###### priority queue ########


class Priority_Queue:
    def create_queue(self):
        self.q=[]
    def enqueue(self,e):
        self.q.append(e)
        self.q.sort(reverse=True)
        print("Enqueued")
    def dequeue(self):#remove and return
        return self.q.pop(0)
    def is_empty(self):#true if len 0 else false
        return len(self.q)==0
    def print_queue(self):
       for item in self.q:
        print(item,end=" - ")
obj=Priority_Queue()
obj.create_queue()
while True:
    print("\nPriority Queue Menu")
    print("------------")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Print")
    print("0.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        obj.enqueue(int(input("Enter element:")))
    elif ch==2:
        if obj.is_empty()!=True:
            print("Dequeued:",obj.dequeue())
        else:
            print("Empty queue")
    elif ch==3:
        if obj.is_empty()!=True:
            obj.print_queue()
        else:
            print("Empty queue")
    elif ch==0:
        print("Exiting....")
        break
    else:
        print("Wrong input")



