#hacker rank simple array sum

import os
import sys

def simpleArraySum(ar,n):
   
     sum = 0

     for i in range(0,n):
        sum+=ar[i]
     return sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    n=len(ar)

    result = simpleArraySum(ar,n)

    fptr.write(str(result) + '\n')

    fptr.close()
