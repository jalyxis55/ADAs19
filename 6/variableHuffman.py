# jalyxis
# Project 6 - Huffman Encoding (Variable Length)
# Spring 2019
# Algorithm Design and Analysis

from heapq import heappush, heappop, heapify
import collections

# findEncoding() - finds the frequency of each character and maps them in a
# dictionary, then assigns the appropriate encoding based on Huffman encoding
# Pre-condition: Takes a dictionary of each character and its frequency
# Post-condition: Returns a dictionary that maps the character to the encoding
def findEncoding(freqDict):
    myHeap = [[freq, [symb, ""]] for symb, freq in freqDict.items()]
    heapify(myHeap)

    while(len(myHeap) > 1):
        low = heappop(myHeap)
        high = heappop(myHeap)

        for pair in low[1:]:
            pair[1] = '0' + pair[1]

        for pair in high[1:]:
            pair[1] = '1' + pair[1]

        heappush(myHeap, [low[0] + high[0]] + low[1:] + high[1:])

    return sorted(heappop(myHeap)[1:], key = lambda p: (len(p[-1]), p))

# encodeTranslate() - Translates plaintext to encoded version
# Pre-condition: String, and dictionary of characters mapped to their encoding
# Post-condition: Encoded string
def encodeTranslate(txt, huffmanCode):
    # tmp variables for encoding
    newStr = ""
    tmpLst = []
    tmpLttr = ""
    val = ""
    k = 0

    # Cycle though txt and build encoded string
    while(k < len(txt)):
        letter = txt[k]
        k += 1

        for i in range(0, len(huffmanCode)):
            tmpLst = huffmanCode[i]
            for j in range(0, len(tmpLst)):
                tmpLttr = tmpLst[j]
                if(letter == tmpLttr):
                    val = tmpLst[j+1]
                    newStr = newStr + val + " "

    return newStr

# decodeTranslate() - Translate encoded text into plaintext
# Pre-condition: takes encoded txt and dictionary of characters mapped to their
# encoding
# Post-condition: Decoded string
def decodeTranslate(encoded, huffmanCode):
    # tmp variables for decoding
    newStr = ""
    binLst = []
    tmpLst = []
    cmp = ""
    tmpStr = ""
    val = ""

    # Split encoded text for decoding
    binLst = encoded.split()

    # Cycle through encoded text and build decoded string
    for i in range(0, len(binLst)):
        cmp = binLst[i]
        for i in range(0, len(huffmanCode)):
            tmpLst = huffmanCode[i]
            tmpStr = tmpLst[1]
            if(cmp == tmpStr):
                val = tmpLst[0]
                newStr = newStr + val

    return newStr

# Driver Function
def main():
    # Variables
    encoded = ""
    decoded = ""

    # Get text to encode from user
    txt = input("Enter text to be encoded: ")

    # Set up frequency dictionary
    freqDict = collections.defaultdict(int)

    # Load user text characters into frequency dictionary
    for c in txt:
        freqDict[c] += 1

    # Count frequency of letters in the user provided text
    freqDict = collections.Counter(txt)

    # Encode each character based on frequency
    huffmanCode = findEncoding(freqDict)

    # Print original text
    print("---Original Text---")
    print(txt, "\n")

    # Print Huffman Encoding for each character
    print("---Huffman Code---")
    print("Symbol\tFreq\tEncoding")
    for i in huffmanCode:
        print("%s\t%s\t%s" % (i[0], freqDict[i[0]], i[1]))

    # Encode and print encoded version
    print("---Encoded Text---")
    encoded = encodeTranslate(txt, huffmanCode)
    print(encoded)

    # Decode and print decoded version
    print("\n---Decoded Text---")
    decoded = decodeTranslate(encoded, huffmanCode)
    print(decoded)

main()
