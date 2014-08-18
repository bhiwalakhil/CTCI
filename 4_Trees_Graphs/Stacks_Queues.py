__author__ = 'akhilbhiwal'

from random import randint

import numpy


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Stack:
    top = None
    count = 0
    minList = []

    def pop(self):
        if self.top != None:
            item = self.top.data
            self.top = self.top.next

            self.count -= 1
            if self.count < self.minList[-1][0]:
                del self.minList[-1]
            return item
        return None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        if not self.minList or data < self.minList[-1][1]:
            self.minList.append((self.count, data))
        self.count += 1
        self.top = node

    def peek(self):
        if self.top:
            return self.top.data

    def getMin(self):
        # print 'minList length: ' + str(len(self.minList))
        return self.minList[-1][1]


class Queue:
    first = None
    last = None

    def enqueue(self, data):
        if self.first == None:
            self.last = Node(data)
            self.first = self.last
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.first != None:
            data = self.first.data
            self.first = self.first.next
            return data
        return None


class Stack_with_Arrays:
    def __init__(self, N, array_size=3):
        self.N = N
        self.array_size = array_size
        self.stack_array = numpy.empty(N * array_size, dtype=int)
        self.stack_array[:] = numpy.NaN

        self.top = numpy.zeros(N + 1, dtype=int)
        for i in range(N + 1):
            self.top[i] = i * array_size

    def push(self, stack, data):
        stack -= 1
        if self.top[stack] == self.array_size * (stack + 1):
            return 'Stack Full. Could not enter data'
        else:
            self.stack_array[self.top[stack]] = data
            self.top[stack] += 1

    def pop(self, stack):
        stack -= 1
        if self.stack_array[self.top[stack]] == numpy.isnan(numpy.nan) or self.top[stack] == self.array_size * stack:
            return None
        else:
            data = self.stack_array[self.top[stack] - 1]
            self.top[stack] -= 1
            return data

    def peek(self, stack):
        stack -= 1
        if self.top[stack] == self.array_size * stack:
            return None
        return self.stack_array[self.top[stack] - 1]


class Queue_with_Stacks:
    stackEnqueue = Stack()
    stackDequeue = Stack()

    def enqueue(self, data):
        self.stackEnqueue.push(data)

    def dequeue(self):
        if self.stackDequeue.peek():
            return self.stackDequeue.pop()
        else:
            while self.stackEnqueue.peek() != None:
                self.stackDequeue.push(self.stackEnqueue.pop())
        return self.stackDequeue.pop()


if __name__ == '__main__':
    stack = Stack()
    stack_num = []

    for i in range(10000):
        number = randint(1, 99999)
        stack.push(number)
        stack_num.append(number)

    # print stack_num
    # print stack.getMin()

    for i in range(5000):
        stack.pop(),
    # print stack.getMin()
    # queue = Queue()
    # queue.enqueue(1)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.enqueue(4)
    # queue.enqueue(5)
    # queue.enqueue(6)
    #
    # stack_with_array = Stack_with_Arrays(3, 3)
    # stack_with_array.push(1, 1)
    # stack_with_array.push(1, 2)
    # stack_with_array.push(1, 3)
    # print stack_with_array.push(1, 6)
    #
    # stack_with_array.push(2, 4)
    # stack_with_array.push(2, 5)
    # stack_with_array.push(2, 6)
    #
    # stack_with_array.push(3, 7)
    # stack_with_array.push(3, 8)
    # stack_with_array.push(3, 9)
    #
    # print stack_with_array.pop(2)
    # print stack_with_array.pop(2)
    # print stack_with_array.pop(2)
    # print stack_with_array.pop(2)
    #
    # print stack_with_array.peek(1)
    # print stack_with_array.peek(2)
    # print stack_with_array.peek(3)

    queue_stack = Queue_with_Stacks()
    for i in range(10):
        queue_stack.enqueue(i)

    for i in range(5):
        print queue_stack.dequeue()

    for i in range(10, 20):
        queue_stack.enqueue(i)

    for i in range(15):
        print queue_stack.dequeue()