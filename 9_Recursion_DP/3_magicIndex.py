__author__ = 'bhiwalakhil'


def hasMagicIndex(input_list, start, end):
    if end < start or start < 0 or end < 0:
        return False
    mid = int((start + end) / 2)

    if end - start <= 1:
        if input_list[start] == start:
            return start
        elif input_list[end] == end:
            return end
        else:
            return False

    if input_list[mid] == mid:
        return mid
    elif input_list[mid] < mid:
        return hasMagicIndex(input_list, start, mid - 1)
    else:
        return hasMagicIndex(input_list, mid, end)


if __name__ == '__main__':
    # input_list = [5,7,9,11,15,16]
    # input_list = [-1, 1, 2, 4, 5, 6]
    # input_list = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    input_list = [0, 0, 0, 0, 0, 0, 0]
    start = 0
    end = len(input_list)
    print hasMagicIndex(input_list, start, end - 1)
