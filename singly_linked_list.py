## This is the constructor for creating a node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # Insert at the end of the list
    def insertLast(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    # Insert at the beginning of the list
    def insertFirst(self, value):
        new_node = Node(value)
        if not self.head:
            self.head=self.tail=new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    # Remove from the end of the list. 2 traversers are used here
    def removeLast(self):
        if not self.head:
            raise ValueError("This LinkedList is Empty!")
        elif self.length == 1:
            val = self.head.data
            self.head = self.tail = None
        else:
            trav1 = self.head
            trav2 = self.head.next
            
            while trav2.next:
                trav1 = trav1.next
                trav2 = trav2.next
            val = trav2.data
            trav1.next = None
            self.tail = trav1
        self.length-=1
        return val
    # Remove from the beginning of the list
    def removeFirst(self):
        if not self.head:
            raise ValueError("LinkedList is Empty!")
        else:
            val = self.head.data
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        self.length-=1
        return val

    ## Remove from the specified position(index)
    def removeAt(self,position):
        if position < 1 or position > self.length:
            raise ValueError("Position out of bound!")
        if position == 1 :
            val = self.removeFirst()
        elif position == self.length:
            val = self.removeLast()
        else:
            trav1 = self.head
            trav2 = self.head.next
            i = 2
            while i < position:
                trav1 = trav1.next
                trav2 = trav2.next
                i+=1
            val = trav2.data
            trav1.next = trav2.next
            trav2.next = None
            self.length-=1
        return val

    ## Insert at a specifeid position
    def insertAt(self, position, value):
        if position < 1 or position > self.length+1:
            raise ValueError("Position out of bound!")
        if position == 1 :
            val = self.insertFirst(value)
        elif position == self.length+1:
            val = self.insertLast(value)
        else:
            trav1 = self.head
            trav2 = self.head.next
            i = 2
            while i<position:
                trav1 = trav1.next
                trav2 = trav2.next
                i+=1
            new_node = Node(value)
            trav1.next = new_node
            new_node.next = trav2
            self.length+=1
            
    def getDetails(self):
        print(self)
        if not self.head:
            print("Empty List")
        else:
            print(f"Length : {self.length}")
            print(f"data at Head : {self.head.data}")
            print(f"data at Tail : {self.tail.data}")

    # Print the linked list as a string
    def __str__(self):
        current = self.head
        temp = ""
        while current:
            #print("hi")
            temp+=str(current.data)+"--> "
            current = current.next
        return temp[:-4]
            
