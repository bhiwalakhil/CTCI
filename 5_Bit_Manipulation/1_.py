__author__ = 'bhiwalakhil'

# Returns True if bit at i is 1, False otherwise.
def getBit(num, i):
    return (num & (1 << i) != 0)


def setBit(num, i):
    return (num | (1 << i))


def clearBit(num, i):
    mask = ~(1 << i)
    return num & mask


def clearBitsMSBthroughI(num, i):
    mask = (1 << i) - 1
    return num & mask


def clearBitsIthrough0(num, i):
    mask = ~(-1 >> (31 - i))
    return num & mask


def updateBit(num, i, v):
    mask = ~(1 << i)
    return (num & mask) | (v << i)


def fitMintoN(N, M, i, j):
    mask = 1 << j - i + 1
    mask = ~(mask << i)
    N = N & mask
    M = M << i
    N = N | M
    return N


def bitFlipsForAToB(A, B):
    C = A ^ B
    count = 0
    while C:
        count += 1
        C = C & (C - 1)
    return count


def swapEvenOddBits(num):
    return (((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1 ))


def drawHorizontalLine(screen, width, x1, x2, y):
    height = len(screen) / width
    mask = ~(1 << (x2 - x1 + 1))
    return screen | mask << (len(screen) - (width * (height - y)))


if __name__ == '__main__':
    N = int('10000000000', 2)
    M = int('10011', 2)
    i = 2
    j = 6

    # print fitMintoN(N, M, i, j)

    A = int('11101001', 2)
    B = int('01111110', 2)
    print bitFlipsForAToB(A, B)