__author__ = 'akhilbhiwal'


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    head = None
    curr = None
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
            self.head = node
        if self.curr:
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
        node = self.head.next
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

    def kthElement(self, k):
        if k < 1:
            return
        node1 = self.head
        node2 = self.head
        count = 0
        while node2:
            node2 = node2.next
            count += 1
            if count > k:
                node1 = node1.next
        if count > k:
            return node1.data
        return

    def partitionList(self, x):
        smallerList = LinkedList()
        biggerList = LinkedList()
        node = self.head

        while node:
            if node.data < x:
                smallerList.addNode(node.data)
            else:
                biggerList.addNode(node.data)
            node = node.next

        smallerList.head = smallerList.head.next
        smallerList.tail.next = biggerList.head.next
        smallerList.display()
        return smallerList


def listSum(list1, list2, order='reverse'):
    num1 = ''
    num2 = ''

    node = list1.head
    while node:
        num1 += str(node.data)
        node = node.next

    node = list2.head
    while node:
        num2 += str(node.data)
        node = node.next

    if order == 'reverse':
        num1 = num1[::-1]
        num2 = num2[::-1]
    return int(num1) + int(num2)


def isCircular(list1):
    node1 = list1.head.next
    node2 = list1.head.next

    while node1 and node2:
        print node1.data, node2.data
        node1 = node1.next
        node2 = node2.next.next

        if node1 == node2:
            return True
    return False


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.addNode(2)
    ll.addNode(9)
    ll.addNode(10)
    ll.addNode(5)
    ll.addNode(6)
    ll.addNode(5)
    ll.addNode(6)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(7)
    ll.addNode(8)
    ll.addNode(9)
    ll.addNode(10)
    ll.display()
    # print ll.search(6)
    # # print ll.deleteNode(8)
    # # ll.removeDuplicates()
    # # ll.removeDuplicatesWithoutBuffer()
    # print ll.kthElement(11)
    # ll.display()
    # ll.partitionList(5)

    l1 = LinkedList(6)
    # l1.addNode(6)
    l1.addNode(1)
    l1.addNode(7)

    l2 = LinkedList(2)
    # l2.addNode(2)
    l2.addNode(9)
    l2.addNode(5)

    print listSum(l1, l2, 'forward')

    cl = LinkedList()
    cl.addNode('A')
    cl.addNode('B')
    cl.addNode('C')
    cl.addNode('D')
    cl.addNode('E')
    cl.addNode('C')
    print isCircular(cl)