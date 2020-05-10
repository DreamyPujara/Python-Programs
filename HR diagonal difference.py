#diagonal difference in hacker rank

import math
import os
import random
import re
import sys

def diagonalDifference(arr):

   #straight diagonal
    fst =0
    sec =0
    length = len(arr[0])
    for count in range(length):
        fst += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(fst-sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
