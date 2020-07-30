# Jennifer Shelby
# Project 7 - Dynamic Programming Matrix Multiplication
# Spring 2019
# Algorithm Design and Analysis

import sys

# mChain() - Performs matrix chain multiplication
# Pre-condition: An array (x) whose elements are row and column sizes (y)
# of matricies to multiply
# Post-condition: 
def mChain(arr, y):
    # temp Variables
    tmp = []
    row = []

    # Load tmp matrix with dummy data
    tmp = [[0 for x in range(y)] for x in range(y)]

    # Test Line
    #print (tmp)

    # Base case - cost is 0
    for i in range (1, y):
        tmp[i][i] = 0

    # Matrix Chain
    for cLen in range (2, y):
        for i in range(1, y-cLen+1):
            j = i+cLen-1
            tmp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = tmp[i][k] + tmp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                # Test Line
                print(cost, "\n")
                if cost < tmp[i][j]:
                    tmp[i][j] = cost

            # Test Lin
            #print(cost)

    return tmp[1][y-1]

# Driver function
def main():
    arr = [30, 35, 15, 5, 10, 20, 25]
    SIZE = len(arr)

    print("Minimum number of multiplications is " + str(mChain(arr, SIZE)))

main()
