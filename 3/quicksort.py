# jalyxis
# Project 3 - Quicksort
# Spring 2019
# Algorithm Design and Analysis

import random

# partition() - Rearranges the subarray arr[p...r] in place
# Pre-condition: takes an array, starting index (p) and pivot index (r)
# Post-condition: returns index
def partition(arr, p, r):
    # Counter
    pCnt = 0

    # tmp variables
    tmp = 0
    tmp2 = 0

    # Pivot
    x = arr[r]
    i = p-1

    for j in range(p, (r-1)):
        if (arr[j] <= x):
            i = i + 1
            # Excchange arr[i] and arr[j]
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            pCnt += 1
    pCnt += 1

    # Exchange arr[i+1] with arr[r]
    tmp2 = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = tmp2

    # Print Counter
    print("Partition Counter: ", pCnt)

    # Print MidPoint
    # print("Midpoint: ", (i+1))

    return i+1

# quicksort() - Recursively performs quicksort on an array
# Pre-condition: takes an array and two indicies
# Post-condition: sorted version of the array
def quicksort(arr, p, r):
    # Counters
    parCnt = 0
    qsCnt = 0

    # Midpoint variable
    q = 0

    if(p < r):
        q = partition(arr, p, r)
        # print("Partition Called: ", arr)
        parCnt += 1
        # Sorts left side of the array from q (pivot index)
        quicksort(arr, p, (q-1))
        # print("Left Quicksort: ", arr)
        qsCnt += 1
        # Sorts right side of array from q (pivot index)
        quicksort(arr, (q+1), r)
        # print("Right Quicksort: ", arr)
        qsCnt += 1

    # Print Counters
    print("Called partition() Counter: ", parCnt)
    print("Quicksort Counter: ", qsCnt)

# Driver Function
def main():
    # Lists
    myList = []
    wcList = []

    # Random size for the list
    SIZE = random.randint(4, 30)

    # Load list with random integers
    for i in range(SIZE):
        myList.append(random.randint(0, 100))

    # Load wcList from random myList
    for i in range(0, len(myList)):
        wcList.append(myList[i])

    # Sort wcList in ascending order (this is worst case for quicksort)
    # using built in list.sort() function
    wcList.sort()

    # Output
    print("N = ", SIZE)

    print("Original Array: ", myList)

    # Sort list with quicksort
    quicksort(myList, 0, (SIZE-1))

    print("Sorted Array: ", myList)

    # Worst case
    print("\n---Worst Case---")
    print("Worst Case: ", wcList)

    # Sort worst-case list with quicksort
    quicksort(wcList, 0, (SIZE-1))

    print("Sorted Worst-Case List: ", wcList)

main()
