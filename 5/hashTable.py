# jalyxis
# Project 5 - Hash Table
# Spring 2019
# Algorithm Design and Analysis

import random

# m = 61
# n = 125
# H(k) = (m*(k*(A%1)))
# A = (5**(1/2) - 1)/2

# search() - searches the studentID dictionary for an sid
# Pre-condition: Takes an sid (student ID number)
# Post-condition: Returns a boolean if the sid is in the dictionary
def search(studentID, sid):
    A = (5**(1/2) - 1)/2
    m = 61
    k = int((m*(sid*(A%1))))
    default = "The student ID is NOT in the Hast Table"
    tmp = studentID.get(k)

    if(sid == tmp):
        return True
    else:
        return False

# Driver Function
def main():
    # Search Constant
    ITR = 10
    
    # Hash function
    A = (5**(1/2) - 1)/2
    n = 125
    m = 61

    # Variables
    sid = 0
    key = 0
    find = 0

    # Dictionary of Student IDs
    studentID = {}

    # List of sid
    sidList = []

    here = False

    # Load list with student ID's
    for i in range(n):
        sidList.append(random.randint(1000, 9999))

    # Sort student ID list in ascending order
    sidList.sort()

    # Add student to dictionary using a hash function for the mapping
    for j in range(n):
        sid = sidList[j]
        key = int((m*(sid*(A%1))))
        studentID[key] = sid

    # Print Student ID List
    print("---Student ID List---")
    print(sidList, sep = "\n")

    # Print Student ID Hash Table
    print("---Student Hash Table---")
    print(studentID, sep = "\n")

    # Loop to search a number of times
    for i in range(ITR):
        find = int(input("Enter StudentID: "))
        here = search(studentID, find)

        if(here):
            print("The student ID is in the Hash Table")

main()
