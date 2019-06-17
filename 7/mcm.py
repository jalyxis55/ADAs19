# Jennifer Shelby
# Project 7 - Matrix Chain Multiplication
# Spring 2019
# Algorithm Design and Analysis

import sys

# mChain() - Finds optimum matrix chain multiplication
# Pre-condition - An array of matrix chains
# Post-conditions returns m and s 
def mChain(arr):
    # Variables
    n = len(arr)
    m = []
    s = []

    # Load m and s with dummy values
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    # Base case
    for i in range(1, n):
        m[i][i] = 0

    # Matrix chaining
    for cLen in range(2, n):
        for i in range(1, (n-cLen+1)):
            j = i + cLen - 1
            # sys.maxsize used as sentinel value
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + arr[i-1] * arr[k] * arr[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s, m[1][n-1]

# printOpt() - Prints the optimal parenthesization
# Pre-condition: takes s and starting and ending values for the number of matricies
# Post-condition: None
#def printOpt(s, i, j):
    #if i == j:
        #print(s[0])
    #else:
        #print("(")
        #printOpt(s, i, s[i][j])
        #printOpt(s, (s[i][j]+1), j)
        #print(")")

# Driver Function
def main():
    arr = [32, 20, 14, 48, 3, 62, 27]
    n = len(arr)

    A = "32 x 20"
    B = "20 x 14"
    C = "14 x 48"
    D = "48 x 3"
    E = "3 x 62"
    F = "62 x 27"

    print("---Matricies---", A, B, C, D, E, F, sep = "\n")

    m, s, minCost = mChain(arr)

    print("\nMinimum Cost: ", minCost)

    print("\n---m---")
    for i in range(len(m)):
        print(m[i])
    print("\n\n")
    print("---s---")
    for i in range(len(s)):
        print(s[i])

    #printOpt(s, 0, (n-1))

main()
