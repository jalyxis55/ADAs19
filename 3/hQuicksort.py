# jalyxis
# Project 3 - Hoare Quicksort
# Spring 2019
# Algorithm Design and Analysis

import random

# hPartition() - Hoare partition
# Pre-condition: array, two indicies
# Post-condition: Returns index of midpoint of the subarray
def hPartition(arr, p, r):
    x = arr[p]
    i = p
    j = r

    # tmp Variable
    tmp = 0

    while(arr[j] > x):
        j = j - 1

    while(arr[i] < x):
        i = i - 1

    if(i < j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    else:
        print(type(j))
        return j

# hQuicksort() - Recursively performs quicksort on an array
# Pre-condition: takes an arry and two indicies
# Post-condition: sorted version of the array
def hQuicksort(arr, p, r):
    # Counters
    parCnt = 0
    qsCnt = 0

    # tmp Variable for midpoint
    q = 0

    if(p < r):
        q = hPartition(arr, p, r)
        parCnt += 1

        # Sorts left side of array from q (pivot index)
        hQuicksort(arr, p, q)
        qsCnt += 1

        # Sorts right side of array from q (pivot index)
        hQuicksort(arr, (q+1), (r-1))
        qsCnt +=1

    # Print Counters
    print("Called hPartition() Counter: ", parCnt)
    print("Quicksort Counter: ", qsCnt)

# Driver Function
def main():
    # Constant for start index of array
    START = 0

    # List
    myList = []

    # Random size for the list
    SIZE = random.randint(4, 30)

    # Load list with random integers
    for i in range(SIZE):
        myList.append(random.randint(0, 100))

    # Output
    print("---USING HOARE PARTITION---")
    print("N = ", SIZE)

    print("Original Array: ", myList)

    hQuicksort(myList, 0, (SIZE-1))

    print("Sorted Array: ", myList)

main()
