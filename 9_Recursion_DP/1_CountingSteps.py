__author__ = 'bhiwalakhil'


def countingSteps(N):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        return countingSteps(N - 1) + countingSteps(N - 2) + countingSteps(N - 3)


def countingStepsDP(N, stepsArray):
    if N < 0:
        return 0
    elif N == 0:
        return 1
    elif stepsArray[N] > -1:
        return stepsArray[N]
    else:
        stepsArray[N] = countingStepsDP(N - 1, stepsArray) + countingStepsDP(N - 2, stepsArray) + countingStepsDP(N - 3,
                                                                                                                  stepsArray)
    return stepsArray[N]


if __name__ == '__main__':
    N = 37
    arrMap = [-1 for i in xrange(N + 1)]
    print countingStepsDP(N, arrMap)
    # print countingSteps(N)