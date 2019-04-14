# jalyxis
# Project 1 - Insertion Sort
# Spring 2019
# Algorithm Design and Analysis

import random

# insertSort()
# Pre-conditions: Takes a list as an argument
# Post-conditions: List will be sorted in place (ascending order) and returns counters
def insertSort(unsorted):
    # Variables for key and indicies
    key = 0
    i = 0
    j = 0

    # Counters
    kCount = 0
    indexCount = 0
    unCount = 0
    jCount = 0
    nKeyCount = 0
    flCount = 0
    wCount = 0

    # for loop to go through the list and sort
    for i in range (0, len(unsorted)):
        key = unsorted[i]
        kCount += 1
        j = i
        indexCount += 1

        # Move elements that are greater than key to (current position + 1)
        while(j > 0 and unsorted[j-1] > key):
            unsorted[j] = unsorted[j-1]
            unCount += 1
            j -= 1
            jCount += 1
            wCount += 1

        unsorted[j] = key
        nKeyCount += 1
        flCount += 1

    # Return counters as a 7-Tuple
    return (kCount, indexCount, unCount, jCount, nKeyCount, flCount, wCount)

# Driver Function
def main():
    # List to be sorted
    myList = []
    wcList = []

    # Random size for list
    SIZE = random.randint(10, 30)

    # Load list with random integers
    for i in range(SIZE):
        myList.append(random.randint(0, 100))

    # Load worst-case list from random myList
    for i in range(0, len(myList)):
        wcList.append(myList[i])

    # Use list.sort() method to sort the elements into reverse order (when worst
    # case occurs for insertion sort)
    wcList.sort(reverse = True)

    # Counters
    kCount = 0
    indextCount = 0
    unCount = 0
    jCount = 0
    nKeyCount = 0
    flCount = 0
    wCount = 0
    total = 0
    wcTotal = 0

    # Print size of list
    print("N = ", SIZE)

    # Print Unsorted List
    print("Unsorted: ", myList)

    # Sort list
    kCount, indexCount, unCount, jCount, nKeyCount, flCount, wCount = insertSort(myList)

    # Calculate Total
    total = kCount + indexCount + unCount + jCount + nKeyCount + flCount + wCount

    # Print Sorted List, Counters, and Total T(n)
    print("Sorted: ", myList)

    print("\n---Counters---")
    print("Set Key: ", kCount)
    print("Set Index: ", indexCount)
    print("Move Element: ", unCount)
    print("Decrement Index: ", jCount)
    print("Set New Key: ", nKeyCount)
    print("For Loop Counter: ", flCount)
    print("While Loop Counter: ", wCount)
    print("T(n) = ", total)

    # Print Worst Case
    print("\nWorst Case: ", wcList)

    # Sort worst-case list
    kCount, indexCount, unCount, jCount, nKeyCount, flCount, wCount = insertSort(wcList)

    # Calculate worst-case total
    wcTotal = kCount + indexCount + unCount + jCount + nKeyCount + flCount + wCount

    # Print sorted worst-case list
    print("Sorted Worst-Case: ", wcList)

    print("\n---Worst Case Counters---")
    print("Set Key: ", kCount)
    print("Set Index: ", indexCount)
    print("Move Element: ", unCount)
    print("Decrement Index: ", jCount)
    print("Set New Key: ", nKeyCount)
    print("For Loop Counter: ", flCount)
    print("While Loop Counter: ", wCount)
    print("T(n) = ", wcTotal)

main()
