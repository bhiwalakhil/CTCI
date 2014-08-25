__author__ = 'bhiwalakhil'


def countOnes(num):
    count = 0
    while num:
        count += 1
        num = num & (num - 1)
    return count


if __name__ == '__main__':
    A = int('11101001', 2)
    num = int('11110101000', 2)
    B = int('01111110', 2)
    print countOnes(num)