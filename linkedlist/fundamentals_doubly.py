class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def traversal(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")
    def convert(self, arr):
        if not arr:
            self.head = None
            return
        self.head = Node(arr[0])
        temp = self.head
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            temp.next = new_node
            new_node.prev = temp
            temp = new_node
# dll = DoublyLinkedList()
# dll.convert([10,20,30])
# dll.traversal()

# delete tail of doubly linkedlist
    def delete_tail(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.delete_tail()
# dll.traversal()

# delete head of doubly linkedlist
    def delete_head(self):
        if self.head is None:
            print("list is empty")
            return
        self.head = self.head.next
        self.head.next.prev = None
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.delete_head()
# dll.traversal()

# delete kth element of doubly linkedlist
    def delete_kth(self,k):
        if self.head is None and k< 1:
            print("invalid position")
            return
        if k==1:
            self.delete_head()
            return
        temp = self.head
        for i in range(k-2): # this excatly stops the loop at k-1
            if temp is None:
                print("invalid position")
                return
            temp = temp.next
        if temp is None and temp.next is None:
            print("invalid position")
            return
        target = temp.next
        temp.next = target.next
        if target.next is not None:
            target.next.prev = temp
        
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.delete_kth(2)
# dll.traversal()

# removing given node in doubly linkedlist
    def remove(self, X):
        if self.head is None:
            return
        temp  = self.head
        while temp:
            if temp.data == X:
                temp.prev.next = temp.next
                return
            temp = temp.next
        print("value not found")
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.remove(30)
# dll.traversal()

# Insert node before head in Doubly Linked List
    def insert_bhead(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.insert_bhead(5)
# dll.traversal()

# Insert node before tail in Doubly Linked List
    def insert_btail(self,data):
        new_node = Node(data)
        if self.head is None:
            return
        if self.head.next is None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head =new_node
        temp = self.head
        while temp.next:
            temp = temp.next
        second_last = temp.prev
        new_node.next = temp
        temp.prev = new_node
        new_node.prev = second_last
        second_last.next = new_node
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.insert_btail(15)
# dll.traversal()

# Insert node before (kth node) in Doubly Linked List
    def insert_bkth(self,k,data):
        new_node = Node(data)
        if self.head is None and k<1:
            return
        if k == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        
        for i in range(k-2):
            if temp is None:
                return
            temp = temp.next
        if temp is None and temp.next is None:
            return
        target = temp.next
        new_node.next = target
        target.prev = new_node
        temp.next = new_node
        new_node.prev = temp
# dll = DoublyLinkedList()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# dll.head = node1
# dll.traversal()
# dll.insert_bkth(2, 17)
# dll.traversal()

# Insert before given node in Doubly Linked List
    def insert_bnode(self,X,data):
        new_node = Node(data)
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == X:
                store = temp.prev
                store.next = new_node
                new_node.next = temp
                temp.prev = new_node
                return
            temp = temp.next
        print("value not found")
dll = DoublyLinkedList()
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
dll.head = node1
dll.traversal()
dll.insert_bnode(20, 18)
dll.traversal()

        


        




        





        


    



