__author__ = 'akhilbhiwal'

import re


def uniqueChar(string):
    string = ''.join(sorted(string))
    temp = ''
    for ch in string:
        if temp == ch:
            return False
        else:
            temp = ch
    return True


def stringReverse(string):
    return string[::-1]


def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    string1 = ''.join(sorted(string1))
    string2 = ''.join(sorted(string2))

    if string1 == string2:
        return True
    return False


def replaceChar(toBeReplaced, sub, string):
    string = re.sub('\s', '%20', string)
    return string


def stringCompression(string):
    count = 0
    compressedString = ''
    ch = string[0]
    for chr in string:
        if ch == chr:
            count += 1
        else:
            compressedString += ch + str(count)
            ch = chr
            count = 1
    compressedString += ch + str(count)
    if len(compressedString) < len(string):
        return compressedString
    else:
        return string


def createTestMatrix(N, M):
    matrix = []
    for i in range(N):
        row = []
        for j in range(M):
            cell = (i + 1, j + 1)
            row.append(cell)
        matrix.append(row)
    return matrix


def printMatrix(matrix):
    N = len(matrix)
    M = len(matrix[0])
    for i in range(N):
        for j in range(M):
            print matrix[i][j],
        print '\n'


# For inplace sorting in a matrix. Without using another matrix. NOT WORKING!
def imageRotation2(matrix):
    N = len(matrix)
    temp1, temp2 = 0, 0
    for row in range(int(N / 2) + 1):
        for col in range(int(N / 2) + 1):
            temp = matrix[row][col]
            temp2 = matrix[N - row - 1][col]
            temp3 = matrix[N - row - 1][N - col - 1]
            matrix[row][col] = matrix[row][N - col - 1]
            matrix[N - row - 1][col] = temp
            matrix[N - row - 1][N - col - 1] = temp2
            matrix[row][N - col - 1] = temp3
    return matrix


def imageRotation(matrix):
    N = len(matrix)
    rotatedMatrix = [[0 for x in range(N)] for y in range(N)]
    for row in range(N):
        for col in range(N):
            rotatedMatrix[col][N - row - 1] = matrix[row][col]
    rotatedMatrix = [y[::-1] for y in rotatedMatrix][::-1]
    return rotatedMatrix


def setRowZero(row, M, matrix):
    for i in range(M):
        matrix[row][i] = 0


def setColZero(N, col, matrix):
    for i in range(N):
        matrix[i][col] = 0


def setRowColZero(matrix):
    N = len(matrix)
    M = len(matrix[0])
    rowList = set()
    colList = set()
    for row in range(N):
        for col in range(M):
            if matrix[row][col] == 0:
                rowList.add(row)
                colList.add(col)
                break
    for row in rowList:
        setRowZero(row, M, matrix)
    for col in colList:
        setColZero(N, col, matrix)
    return matrix


def isRotation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = string1 + string1
    if string1.find(string2) >= 0:
        return True


if __name__ == '__main__':
    print '1.1 - Unique characters in a string.'
    print uniqueChar('Jaipur')
    print uniqueChar('Hello')

    print '\n1.2 - Reverse a string.'
    print stringReverse('Jaipur')
    print stringReverse('12345')

    print '\n1.3 - String Permutation'
    print checkPermutation('waterbottle', 'terbottlewa')
    print checkPermutation('hello', 'lleho')
    print checkPermutation('ehllow', 'wrodld')

    print '\n1.4 - Replace spaces with %20.'
    print replaceChar('a', 'a', 'Mr John Smith')
    print replaceChar('a', 'a', 'Akhil Bhiwal')

    print '\n1.5 - String Compression.'
    print stringCompression('aabcccccaaa')
    print stringCompression('aabbccaa')

    print '\n1.6 - Image Rotation.'
    print imageRotation(createTestMatrix(3, 3))
    print imageRotation(createTestMatrix(5, 5))

    print '\n1.7 - Setting Row and Column Zero.'
    matrix34 = createTestMatrix(3, 4)
    matrix34[0][2] = 0
    matrix34[2][2] = 0
    # printMatrix(matrix34)
    printMatrix(setRowColZero(matrix34))

    print '\n1.8 - String Rotation.'
    print isRotation('waterbottle', 'erbottlewat')