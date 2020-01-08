# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&limit=50&page=1&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    notDone = True
    jumps = 0
    size = len(c) - 1
    current = 0

    while(current < size):
        if (((current + 2) <= size) and (c[current+2] == 0)):
            jumps = jumps + 1
            current = current + 2
            print("double")
            print(current)
        else:
            jumps = jumps + 1
            current = current + 1
            print("single")
            print(current)


    return jumps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
