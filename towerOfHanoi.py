__author__ = 'kaushikn'

from Stacks_Queues import Stack

class TowerOfHanoi:
    towerSrc = Stack()
    towerInter = Stack()
    towerDes = Stack()
    tSrcpeek = None
    tInterpeek = None
    tDespeek = None

    def __init__(self, *args):
            print elem
            self.towerSrc.push(elem)
        self.updatePeek()

    def printTop(self):
        print 'TowerSrc: ' + str(self.towerSrc.peek())
        print 'TowerInter: ' + str(self.towerInter.peek())
        print 'TowerDes: ' + str(self.towerDes.peek())

    def move(self, towerFrom, towerTo):
        if towerFrom.peek():
            towerTo.push(towerFrom.pop())
        self.updatePeek()

    def updatePeek(self):
        self.tDespeek = self.towerSrc.peek()
        self.tInterpeek = self.towerInter.peek()
        self.tSrcpeek = self.towerDes.peek()

    def solve(self, n, towerSrc, towerDes, towerInter):
        if n == 0:
            return
        if n == 1:
            self.move(towerSrc, towerDes)
        if n >= 2:
            self.solve(n-1, towerSrc, towerInter, towerDes)
            self.move(towerSrc, towerDes)
            self.solve(n-1, towerInter, towerDes, towerSrc)
        self.printTop()

    def outerSolve(self, n):
        self.solve(n, self.towerSrc, self.towerDes, self.towerInter)

if __name__=='__main__':
    N = 5
    arg = []
    for i in range(N, 0, -1):
        arg.append(i)
    towerOfHanoi = TowerOfHanoi(*arg)
    towerOfHanoi.outerSolve(N)