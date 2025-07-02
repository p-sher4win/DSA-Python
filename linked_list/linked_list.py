# Create a node
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# Create a Linked List
class LinkedList:
    def __init__(self):
        # Empty Linked List
        self.head = None
        self.n = 0

    # return the size of LL
    def __len__(self):
        return self.n
    
    # Insert a node at head
    def insert_head(self, value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        # reassign head
        self.head = new_node

        # increment n by 1
        self.n += 1

    # Print the data in Linked List
    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result+=str(curr.data)+"->"
            curr = curr.next

        return result[:-2] if result!='' else 'Empty Linked List'
    
    # append node at the tail
    def append(self, value):
        new_node = Node(value)

        # when empty linked list
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        curr = self.head

        while curr.next != None:
            curr = curr.next
        
        # your are at the last node and append the new node
        curr.next = new_node
        self.n += 1

    # insert node in between the nodes
    def insert_between(self, after, value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n+=1
        else:
            return 'Item not found'
        
    # Clear linked list
    def clear(self):
        self.head = None
        self.n = 0

    # Delete head node
    def delete_head(self):
        if self.head != None:
            self.head = self.head.next
            self.n-=1
        else:
            return 'Empty Linked List'
        
    # Pop a node
    def pop(self):
        # only if zero node
        if self.head == None:
            return 'Empty Linked List'

        curr = self.head
        
        # only if one node
        if curr.next == None:
            return self.delete_head()

        # only more than one nodes
        while curr.next.next != None:
            curr = curr.next

        # we reach on the 2nd last node
        curr.next = None
        self.n-=1

    # delete by value
    def remove(self, value):
        if self.head == None:
            return 'Empty Linked List'

        if self.head.data == value:
            return self.delete_head()

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        
        if curr.next == None:
            return 'Item Not Found'
        else:
            curr.next = curr.next.next
            self.n-=1

    # search node data
    def search(self, value):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == value:
                return pos
            curr = curr.next
            pos+=1
        
        return 'Not Found'
    
    # search by index
    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos+=1

        return 'IndexError'
    
    # delete node by index
    def delete_index_node(self, index):
        curr = self.head
        pass


L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(L)
print(len(L))

# L.append(5)
# print(L)
# print(len(L))

# L.append(6)
# print(L)
# print(len(L))

# L.insert_between(2, 200)
# print(L)
# print(len(L))

# L.clear()
# print(L)
# print(len(L))

# L.delete_head()
# print(L)
# print(len(L))
# L.delete_head()
# print(L)
# print(len(L))
# L.delete_head()
# print(L)
# print(len(L))
# L.delete_head()
# print(L)
# print(len(L))

# L.pop()
# print(L)
# print(len(L))
# L.pop()
# print(L)
# print(len(L))
# L.pop()
# print(L)
# print(len(L))
# L.pop()
# print(L)
# print(len(L))
# L.pop()
# print(L)
# print(len(L))
# L.pop()
# print(L)
# print(len(L))

# L.remove(3)
# print(L)
# print(len(L))
# L.remove(10)
# print(L)
# print(len(L))
# L.remove(1)
# print(L)
# print(len(L))
# L.remove(2)
# print(L)
# print(len(L))
# L.remove(4)
# print(L)
# print(len(L))
# L.remove(10)
# print(L)
# print(len(L))

# print(L.search(1))

# print(L[1])
































# Manual creation of Linked List
# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c
# print(a)
# print(a.next)
# print(b)
# print(b.next)
# print(c)
# print(c.next)