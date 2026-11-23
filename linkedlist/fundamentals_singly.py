class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        
# Traversal and print the ll
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")

# insert at head
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# insert at tail
    def insert_tail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
# ll = Linkedlist()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.insert_head(5)
# ll.insert_tail(40)
# ll.traversal()

# insert at kth position
    def insert_k(self, data, k):
        if k < 1:
            print("invalid pos")
            return
        if k == 1:
            self.insert_head(data)
            return
        temp = self.head
        for i in range(k-2):
            if temp is None:
                print("invalid pos")
                return
            temp = temp.next
        if temp is None:
            print("invalid pos")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
# ll = Linkedlist()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.insert_head(5)
# ll.insert_tail(40)
# ll.insert_k(50,2)
# ll.traversal()

# insert before value X
    def insert_bX(self,data, X):
        if self.head is None:
            print("list is empty")
            return
        if self.head == X:
            self.insert_head(data)
            return
        temp = self.head
        while temp.next:
            if temp.next.data == X:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next  = new_node
                return
            temp = temp.next
        
        print("value not found")
# ll = Linkedlist()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.insert_head(5)
# ll.insert_tail(40)
# ll.insert_k(50,2)
# ll.insert_bX(60, 30)
# ll.traversal()

# delete head node
    def delete_head(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next
# ll = Linkedlist()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.insert_head(5)
# ll.insert_tail(40)
# ll.insert_k(50,2)
# ll.insert_bX(60, 30)
# ll.delete_head()
# ll.traversal()

# delete tail node
    def delete_tail(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

# delete at kth position

    def delete_kth(self,k):
        
        if k < 1 and self.head is None:
            print("invalid position")
            return
        if k == 1:
            self.head = None
            return
        temp = self.head
        for i in range(k-1):
            if temp is None:
                print("invalid position")
                return
            temp = temp.next
        if temp.next is None:
            print("invalid position")
            return
        temp.next = temp.next.next


# delete node with value X
    def delete_x(self, X):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == X:
            self.head = self.head.next
            return
        temp = self.head
        while temp is not None and temp.next is not None: # we use here temp is not none condition because when we reach at the end of linkedlist temp become none
            if temp.next.data == X:
                temp.next = temp.next.next
            temp = temp.next

# find the length of linkedlist
    def length_ll(self):
        c = 0
        if self.head is None:
            return c
        temp = self.head
        while temp is not None:
            c += 1
            temp = temp.next
        return c


# search in linkedlist
    def search(self, X):
        if self.head is None:
            print("list is empty")
            return
        temp = self.head
        while temp is not None:
            if temp.data == X:
                print("value found")
                return # we have to add this return here so that if we have found our value it will immediately exit the function by this call
            temp = temp.next
        print("value not found") # this will execute only when we will not find any value

ll = Linkedlist()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.insert_head(5)
ll.insert_tail(40)
ll.insert_k(50,2)
ll.insert_bX(60, 30)
ll.delete_head()
ll.traversal()
print(ll.length_ll())
ll.search(15)




    



   


    
    


        














