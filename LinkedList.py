__author__ = 'akhilbhiwal'

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    head = None
    curr = Node()
    tail = None

    def __init__(self, data=None):
        node = Node(data)
        if self.head == None:
            self.head = node
        self.curr = node
        if self.tail == None:
            self.tail = node

    def addNode(self, data):
        node = Node(data)
        if self.head == None:
            head = node
        self.curr.next = node
        self.curr = node
        self.tail = node

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def deleteNode(self, data):
        node = self.head
        prev = node
        while node:
            if node.data == data:
                prev.next = node.next
                return True
            prev = node
            node = node.next
        return False

    def display(self):
        node = self.head
        while node:
            print node.data,
            node = node.next
        print

    def removeDuplicates(self):
        node = self.head
        elem = {}
        while node:
            if node.data not in elem:
                elem[node.data] = 1
            else:
                self.deleteNode(node.data)
            node = node.next

    def removeDuplicatesWithoutBuffer(self):
        node = self.head
        while node:
            node2 = node.next
            while node2:
                if node.data == node2.data:
                    node2.data = node2.next.data
                    node2.next = node2.next.next
                node2 = node2.next
            node = node.next

if __name__=='__main__':
    ll = LinkedList()
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(5)
    ll.addNode(4)
    ll.addNode(5)
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(8)
    ll.display()
    print ll.search(6)
    # print ll.deleteNode(8)
    ll.removeDuplicates()
    ll.removeDuplicatesWithoutBuffer()
    ll.display()
