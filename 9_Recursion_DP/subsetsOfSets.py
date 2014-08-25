__author__ = 'bhiwalakhil'

from itertools import combinations, permutations


def subsetOfSets(mainSet):
    n = len(mainSet)
    print list(permutations(mainSet, n))
    print list(combinations(mainSet, n))
    matching = [c for c in combinations(mainSet, n) if reduce(lambda x, y: x * y, c, 1) == 60]


if __name__ == '__main__':
    setElem = set(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))
    # subsetOfSets(setElem)