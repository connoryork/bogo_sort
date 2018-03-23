__author__ = 'Connor'

from random import *
import time
import math

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
    try:
        for i in range(len(lst)*math.floor(math.log(len(lst, 2)))) :
            n += 1
            bogo_sort(unlst)
            if lst == unlst :
                break
            print(str(n))
        else :
            raise Exception
        endTime = time.clock()
        print("Run", str(n), "passed after", str(endTime - startTime), "seconds!")
    except Exception:
        print("segmentation fault")

if __name__ == "__main__":
    main()
