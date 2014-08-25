__author__ = 'bhiwalakhil'

import numpy as np


def getPaths(X0, Y0, X, Y):
    if X0 == X and Y0 == Y:
        return 0
    elif X0 == X or Y0 == Y:
        return 1
    else:
        return getPaths(X0 + 1, Y0, X, Y) + getPaths(X0, Y0 + 1, X, Y)


def getPathsDP(X0, Y0, X, Y, arrlist):
    if X0 == X and Y0 == Y:
        return 0
    elif X0 == X or Y0 == Y:
        return 1
    elif arrlist[X0][Y0] > -1:
        return arrlist[X0][Y0]
    else:
        if arrlist[X0 + 1][Y0] == -1:
            arrlist[X0 + 1][Y0] = getPathsDP(X0 + 1, Y0, X, Y, arrlist)
        if arrlist[X0][Y0 + 1] == -1:
            arrlist[X0][Y0 + 1] = getPathsDP(X0, Y0 + 1, X, Y, arrlist)
        arrlist[X0][Y0] = arrlist[X0 + 1][Y0] + arrlist[X0][Y0 + 1]
    return arrlist[X0][Y0]


if __name__ == '__main__':
    N = 50
    M = 500
    arrlist = np.tile(-1, (N + 1, M + 1))
    print getPathsDP(0, 0, N, M, arrlist)
    # print getPaths(0,0, N, M)
