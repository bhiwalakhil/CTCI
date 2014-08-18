__author__ = 'bhiwalakhil'


class CircularBuffer:
    size = 0
    head = 0
    tail = 0
    circularBuffer = []

    def __init__(self, size):
        self.size = int(size) + 1

    def enqueue(self, data):
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size - 1):
            if self.head == self.size - 1:
                self.head = 0
            else:
                self.head += 1
        try:
            self.circularBuffer[self.tail] = data
        except:
            self.circularBuffer.append(data)

        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            return None
        try:
            data = self.circularBuffer[self.head]
        except:
            return None
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return data

    def append(self, n):
        for i in range(n):
            self.enqueue(raw_input())

    def remove(self, n):
        for i in range(n):
            self.dequeue()

    def list(self):
        if self.head == self.tail:
            return None
        if self.head < self.tail:
            for i in range(self.head, self.tail):
                print self.circularBuffer[i]
        else:
            for i in range(self.head, self.size):
                print self.circularBuffer[i]
            for i in range(self.tail):
                print self.circularBuffer[i]


if __name__ == '__main__':
    size = raw_input()
    circularBuffer = CircularBuffer(size)
    while True:
        elem = raw_input()
        if elem == 'Q':
            break
        elif elem == 'L':
            circularBuffer.list()
        else:
            elem = elem.split()
            if elem[0] == 'A':
                circularBuffer.append(int(elem[1]))
            elif elem[0] == 'R':
                circularBuffer.remove(int(elem[1]))
            else:
                print 'Error'
                break

