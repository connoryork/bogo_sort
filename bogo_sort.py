__author__ = 'Connor'

from random import *
import time

def bogo_sort(lst):
    r1, r2 = randint(0,len(lst)-1), randint(0,len(lst)-1)
    temp = lst[r1]
    lst[r1] = lst[r2]
    lst[r2] = temp
    return lst

def randomlst():
    lst = []
    while len(lst) <= 10:
        i = randint(-999, 999)
        lst.append(i)
    return lst

def main():
    unlst = randomlst()
    n = 1
    lst = sorted(unlst)
    startTime = time.clock()
    while lst != bogo_sort(unlst):
        n += 1
        print(str(n))
    endTime = time.clock()
    print("Run", str(n), "passed after", str(endTime - startTime), "seconds!")

if __name__ == "__main__":
    main()