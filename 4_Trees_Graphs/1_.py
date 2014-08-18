__author__ = 'bhiwalakhil'

import numpy as np

from Stacks_Queues import Queue
from LinkedList import LinkedList


class Node:
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree:
    root = None

    def __init__(self, data=None):
        self.root = Node(data)

    def traversal(self, method):
        if method == 'preorder':
            self.preorder(self.root)
        elif method == 'postorder':
            self.postorder(self.root)
        else:
            self.inorder(self.root)

    def preorder(self, root):
        if not root:
            return
        print root.data
        if root.lChild:
            self.preorder(root.lChild)
        if root.rChild:
            self.preorder(root.rChild)

    def inorder(self, root):
        if not root:
            return
        if root.lChild:
            self.inorder(root.lChild)
        print root.data
        if root.rChild:
            self.inorder(root.rChild)

    def postorder(self, root):
        if not root:
            return
        if root.lChild:
            self.postorder(root.lChild)
        if root.rChild:
            self.postorder(root.rChild)
        print root.data

    def search(self, data, method):
        if method == 'bfs':
            return self.bfs(data)
        elif method == 'dfs':
            return self.dfs(data)
        else:
            return None

    def bfs(self, data):
        queue = Queue()
        node = self.root
        queue.enqueue(node)
        while node:
            if node.data == data:
                return node
            if node.lChild:
                queue.enqueue(node.lChild)
            if node.rChild:
                queue.enqueue(node.rChild)
            node = queue.dequeue()
        return None

    def dfs(self, root, data):
        node = root
        if node == None:
            return
        elif node.data == data:
            return node
        else:
            self.dfs(node.lChild, data)
            self.dfs(node.rChild, data)

    def insert(self, data, parent, child='l'):
        if not self.root.data:
            self.root.data = data
        else:
            node = self.search(parent, 'bfs')
            if node and child == 'l' and node.lChild == None:
                node.lChild = Node(data)
            elif node and child == 'r' and node.rChild == None:
                node.rChild = Node(data)
            else:
                return None

    def bstInsert(self, data):
        node = self.root
        temp = Node()
        if not node.data:
            self.root = Node(data)
            return
        while node:
            prev = node
            if data <= node.data:
                node = node.lChild
            elif data > node.data:
                node = node.rChild
        node = Node(data)
        if data <= prev.data:
            prev.lChild = node
        else:
            prev.rChild = node

    def isBalanced(self, node=None):
        if not node:
            node = self.root
        left, right = 0, 0
        try:
            if node.lChild:
                left = 1 + self.isBalanced(node.lChild)
            if node.rChild:
                right = 1 + self.isBalanced(node.rChild)
        except:
            return None
        if abs(left - right) > 1:
            return None
        else:
            return max(left, right)

    def insert_using_array(self, arr):
        arr_len = len(arr)
        if arr_len == 0:
            return
        self.bstInsert(arr[arr_len / 2])
        self.insert_using_array(arr[:int(arr_len / 2)])
        self.insert_using_array(arr[int(arr_len / 2) + 1:])

    def four_3(self):
        arr = []
        for i in range(1, 8):
            arr.append(i)
        sorted_array = np.array(arr, int)
        self.insert_using_array(sorted_array)

    def bfsReturningList(self):
        linkedList = LinkedList()
        queue = Queue()
        node = self.root

        ll = LinkedList()
        ll.addNode(node.data)
        linkedList.addNode(ll)

        queue.enqueue(node)
        queue.enqueue('$')

        ll = LinkedList()
        linkedList.addNode(ll)
        node = queue.dequeue()

        while node:
            if node.lChild:
                queue.enqueue(node.lChild)
                ll.addNode(node.lChild.data)
            if node.rChild:
                queue.enqueue(node.rChild)
                ll.addNode(node.rChild.data)

            node = queue.dequeue()
            if node == '$':
                node = queue.dequeue()
                if node:
                    ll = LinkedList()
                    linkedList.addNode(ll)
                    queue.enqueue('$')

        self.printBFSLists(linkedList)
        linkedList.display()

    def printBFSLists(self, linkedList):
        node = linkedList.head.next
        i = 1
        while node:
            print 'List: ' + str(i)
            ll = node.data
            if ll:
                ll.display()
            i += 1
            node = node.next

    def four_4(self):
        self.bfsReturningList()

    def isBST(self):
        node = self.root
        if node is None:
            return True
        if node.lChild <= node.data and node.rChild > node.data:
            flag1 = self.isBST(node.lChild)
            if not flag1:
                return False
            flag2 = self.isBST(node.rChild)
            if not flag2:
                return False
        else:
            return False
        return True

    def four_5(self):
        print self.isBST()


if __name__ == '__main__':
    tree = Tree()

    # tree.insert(1, 1, 'l')
    # tree.insert(2, 1, 'l')
    # tree.insert(3, 1, 'r')
    # tree.insert(4, 2, 'l')
    # tree.insert(5, 2, 'r')
    # tree.insert(6, 3, 'l')
    # tree.insert(7, 3, 'r')
    # tree.insert(8, 4, 'l')
    # tree.insert(9, 8, 'l')

    # print 'Preorder Traversal:'
    # tree.traversal('preorder')
    # print 'Postorder Traversal:'
    # tree.traversal('postorder')
    # print 'Inorder Traversal:'
    # tree.traversal('inorder')

    # print tree.isBalanced()
    tree.four_3()
    # print 'Inorder Traversal:'
    # tree.traversal('inorder')

    # tree.four_4()

    tree.four_5()