__author__ = 'bhiwalakhil'


def readInput():
    rocks = []
    try:
        total_words = int(raw_input())
    except:
        print 'Oops! Is your first line a valid number?\nCurrently, I only understand integers. :('
        print 'exiting'
        exit()

    for i in range(total_words):
        rocks.append(raw_input())
    return rocks


if __name__ == '__main__':
    rocks = readInput()
    elem_set_list = []

    for rock in rocks:
        elem_set = set()
        elem_set.update(elem for elem in rock)
        elem_set_list.append(elem_set)

    gem_elem = set.intersection(*elem_set_list)

    print len(gem_elem)