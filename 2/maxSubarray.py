# jalyxis
# Project 2 - Max Subarray
# Spring 2019
# Algorithm Design and Analysis

import random

# maxCross()
# Pre-conditions: Array and indicies (low, mid, and high)
# Post-conditions: Returns a tuple containing indicies specifying the maximum
# subarray that crosses the midpoint, and the sum of the values in the
# maximum subarray
def maxCross(arr, low, mid, high):
    # Sentinel Constant
    SENTINEL = -1000
    # Counters
    lCnt = 0
    rCnt = 0
    cCnt = 0

    # Sum of both left and right side accumulators
    total = 0

    # Left side accumulators
    lMax = 0
    leftSum = SENTINEL
    accum = 0

    for i in range(mid, low, -1):
        accum += arr[i]
        if(accum > leftSum):
            leftSum = accum
            # Keep left side max index
            lMax = i
            lCnt += 1
        lCnt += 1

    # Right side accumulators
    rMax = 0
    rSum = SENTINEL
    accum = 0

    for j in range ((mid + 1), high):
        accum += arr[j]
        if(accum > rSum):
            rSum = accum
            # Keep right side max index
            rMax = j
            rCnt += 1
        rCnt += 1

    # Find total counts for loops and if statements
    cCnt = lCnt + rCnt

    # Sum of left and right sides
    total = leftSum + rSum

    # Print counters
    print("MaxCross Count: ", cCnt)

    # Return max indicies and sum
    return(lMax, rMax, total)

# maxSubarray()
# Pre-conditions: Array and indicies (low and high)
# Post-conditions: Returns tuple containing the indicies marking the maximum
# subarray and the sum of the values in the maximum subarray
def maxSubarray(arr, low, high):
    # Subarray Counter
    saCnt = 0

    # Left and right side and cross indicies and sum
    lLow = 0
    lHigh = 0
    lSum = 0
    rLow = 0
    rHigh = 0
    rSum = 0
    cLow = 0
    cHigh = 0
    cSum = 0
    cCnt = 0

    # Base Case (N = 1)
    if(high == low):
        saCnt += 1
        print("Max Subarray Count: ", saCnt)
        return (low, high, arr[low])

    # Recursion
    else:
        mid = int((low + high)/2)

        # Find left side max subarray
        lLow, lHigh, lSum = maxSubarray(arr, low, mid)

        # Find right side max subarray
        rLow, rHigh, rSum = maxSubarray(arr, (mid+1), high)

        # Find max cross subarray
        cLow, cHigh, cSum = maxCross(arr, low, mid, high)

        if((lSum >= rSum) and (lSum >= cSum)):
            saCnt += 1
            print("Max Subarray Count: ", saCnt)
            return(lLow, lHigh, lSum)
        elif ((rSum >= lSum) and (rSum >= cSum)):
            saCnt += 1
            print("Max Subarray Count: ", saCnt)
            return(rLow, rHigh, rSum)
        else:
            saCnt += 1
            print("Max Subarray Count: ", saCnt)
            return(cLow, cHigh, cSum)

# Driver Function
def main():
    # List
    myList = []
    
    # Results
    high = 0
    low = 0
    tSum = 0

    # Random size for list
    SIZE = random.randint(5, 8)

    # Load list with random integers
    for i in range(SIZE):
        myList.append(random.randint(-10, 10))

    # Output
    print("N = ", SIZE)

    print("Original Array: ", myList)

    low, high, tSum = maxSubarray(myList, 0, (SIZE-1))

    print("Low: ", low)
    print("High: ", high)

    print("\nSum: ", tSum)
    print("\n\nMax Subarray: ")
    for i in range(low, high):
        print(myList[i])

main()
