class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linear_Linked_List:
    def __init__(self):
        self.root=None #root is not created but assigned
    def insert_left(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n#assigned as first
        else:
            n.next=self.root
            self.root=n
        print("inserted")
    def insert_right(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n#assigned as first
        else:
            t=self.root#1
            while t.next!=None:#2
                t=t.next
            t.next=n
        print("inserted")

    def delete_left(self):
        if self.root==None:
            print("Empty list")
        else:
            t=self.root#1
            self.root=self.root.next#2
            print("Deleted:",t.data)

    def delete_right(self):
        if self.root==None:
            print("Empty list")
        else:
            t=self.root#1
            t2=self.root#1
            while t.next!=None:#2
                t2=t
                t=t.next
            if self.root==t:
                self.root=None
            else:
                t2.next=None#3
            print("Deleted:",t.data)
    def print_list(self):
        if self.root==None:
            print("Empty list")
        else:
            t=self.root
            while t!=None:
                print(f"|{t.data}|->",end="")
                t=t.next
    def len_list(self):
        if self.root==None:
            return 0
        else:
            count=0
            t=self.root
            while t!=None:
                count+=1
                t=t.next
            return count

    def search_list(self,key_element):
        t=self.root#t ref
        while t!=None:#till t not None
            if t.data==key_element:
                return True#if match stop return True
            t=t.next
        return False#return False

    def insert_after(self,ref,new_element):
        t=self.root#t ref
        while t!=None:#till t not None
            if t.data==ref:#if found 2
                n=Node(new_element)
                n.next=t.next#3
                t.next=n#4
                print("inserted..")
                break
            t=t.next
        if t==None:
            print(ref,"not found in list")
    def delete_element(self,element):
        t=self.root#t ref
        t2=self.root
        while t!=None:#till t not None
            if t.data==element:
                if t==self.root:#case 1 :left most
                    self.root=self.root.next
                elif t.next==None:#case 2:right most
                    t2.next=None
                else:#case 3 in-between
                    t2.next=t.next
                print("Deleted:",t.data)
                break
            t2=t
            t=t.next
        if t==None:
            print(element,"not found in list")
    def reverse_list(self):
        if self.root==None:#check list there or not
            print("Empty list")
        else:#list there
            #read all elements and append them to list
            t=self.root
            temp=[]#list
            while t!=None:
                temp.append(t.data)
                t=t.next
            #restart and over write 1st node with last entry of list
            t=self.root
            while t!=None:
                t.data=temp.pop()
                t=t.next
            print("Reversed")
    def sort_list(self):
        if self.root==None:#check list there or not
            print("Empty list")
        else:#list there
            #read all elements and append them to list
            t=self.root
            temp=[]#list
            while t!=None:
                temp.append(t.data)
                t=t.next
            #sort list
            temp.sort(reverse=True)
            #overwrite on linked list
            t=self.root
            while t!=None:
                t.data=temp.pop()
                t=t.next
            print("Reversed")
    def get_root(self):
        return self.root
    def divide_list(self):
        even=Linear_Linked_List()
        odd=Linear_Linked_List()
        t=self.root
        while t!=None:
            if t.data%2==0:
                even.insert_right(t.data)
            else:
                odd.insert_right(t.data)
            t=t.next
        return even,odd

ll = Linear_Linked_List()
while True:
    print("\nMenu:")
    print("1. Insert Left")
    print("2. Insert Right")
    print("3. Delete Left")
    print("4. Delete Right")
    print("5. Print List")
    print("6. Searchin List")
    print("7. Length of list")
    print("8. Insert After")
    print("9. Delete Element")
    print("10.Reverse List")
    print("11.Sort List")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data to insert at left: "))
        ll.insert_left(data)
    elif choice == 2:
        data = int(input("Enter data to insert at right: "))
        ll.insert_right(data)
    elif choice == 3:
        ll.delete_left()
    elif choice == 4:
        ll.delete_right()
    elif choice == 5:
        ll.print_list()
    elif choice == 6:
        print("Found:",ll.search_list(int(input("Enter element to search:"))))
    elif choice == 7:
        print("Length is:",ll.len_list())
    elif choice == 8:
        ll.insert_after(int(input("Enter ref:")),int(input("Enter new element:")))
    elif choice == 9:
       ll.delete_element(int(input("Enter new element:")))
    elif choice == 10:
       ll.reverse_list()
    elif choice == 11:
       ll.sort_list()
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")