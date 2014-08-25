__author__ = 'bhiwalakhil'


def readInput():
    list_input = []
    try:
        test_cases = int(raw_input())
    except:
        print 'Oops! Is your first line a valid number?\nCurrently, I only understand integers. :('
        print 'exiting'
        exit()
    list_input.append(test_cases)
    for i in range(test_cases * 3):
        list_input.append(int(raw_input()))
    return list_input


def computeSteps(n, a, b, final_sum, final_list):
    if n <= 1:
        final_list.append(final_sum)
        return 0
    computeSteps(n - 1, a, b, final_sum + a, final_list)
    computeSteps(n - 1, a, b, final_sum + b, final_list)


if __name__ == '__main__':
    list_input = readInput()
    test_cases = list_input[0]
    # for i in xrange(test_cases):
    # final_list = []
    #     computeSteps(list_input[3*i+1], list_input[3*i+2], list_input[3*i+3], 0, final_list)
    #     for elem in sorted(set(final_list)):
    #         print elem,
    #     print
