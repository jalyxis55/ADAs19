# Jennifer Shelby
# Project 9 - Binary Search Tree
# Spring 2019
# Algorithm Design and Analysis

# Individual Node class
# val is a tuple where the first element is the students position in the list
# the second element is the student ID
class Node:
    def __init__(self, i, sid):
        self.left = None
        self.right = None
        self.val = (i, sid)

# minNode() finds the minimum sid in the tree
# Pre-condition: NON-EMPTY BST
# Post-condition: returns node with minimum sid
def minNode(n):
    minNode = n

    # find leftmost node
    while(minNode.left is not None):
        minNode = minNode.left

    return minNode

# insertNode() inserts a node for a given student using the sid
# Pre-condition: takes the root of the tree and a new node, n
# Post-condition: node is inserted into the tree
def insertNode(root, n):
    # If the tree is empty, new node is root
    if(root is None):
        return n

    # Traverse through tree to find new node's spot
    if(n.val[1] < root.val[1]):
        root.left = insertNode(root.left, n)
    else:
        root.right = insertNode(root.right, n)

    # return root pointer
    return root

# delNode() removes a node for a given student using the sid
# Pre-condition: takes the root and sid of student to be removed from tree
# Post-condition: returns root of the tree
def delNode(root, k):
    # Base case - root is null
    if(root is None):
        return root

    # k is smaller than root.sid then the student must be in the left subtree
    if(k < root.val[1]):
        root.left = delNode(root.left, k)

    # k is larger than root.sid then the student must be in right subtree
    elif(k > root.val[1]):
        root.right = delNode(root.right, k)

    # k equals the root.sid this is node to be deleted
    else:
        # Case if node has no child or one child
        if(root.left is None):
            tmp = root.right
            root = None
            return tmp
        elif(root.right is None):
            tmp = root.left
            root = None
            return tmp

        # Case if node has two children
        tmp = minNode(root.right)

        # Copy content
        root.val = tmp.val

        # Remove node
        root.right = delNode(root.right, tmp.val[1])

    return root

# trav() traverses the tree in order
# Pre-condition: takes the root node
def trav(root, myList):
    if(root is not None):
        trav(root.left, myList)
        tmp = root.val[0]
        print(myList[tmp])
        trav(root.right, myList)

# find() searches the BST for a given student by student ID number
def find(root, k):
    # Base case - root is null
    if(root is None or root.val[1] == k):
        return root

    # k is greater than root's value search right
    if(root.val[1] < k):
        return find(root.right, k)

    # k is less than root's value search left
    else:
        return find(root.left, k)

# Driver
def main():
    # Student Lists
    SHList = [(42563, "Oliver Queen", [55, 76, 84, 43, 67, 48, 72, 85, 66, 58]),
             (68413, "Selina Kyle", [94, 85, 99, 89, 100, 86, 92, 87, 79, 83]),
             (13786, "Barry Allen", [100, 98, 99, 100, 97, 89, 95, 100, 99, 100]),
             (24539, "Barbra Gordon", [100, 100, 100, 100, 100, 100, 100, 100, 98, 100]),
             (55576, "Dick Grayson", [86, 83, 92, 81, 87, 95, 84, 75, 96, 91]),
             (39890, "Clark Kent", [75, 89, 78, 81, 90, 83, 79, 88, 84, 92]),
             (45618, "Bruce Wayne", [96, 98, 82, 85, 100, 73, 88, 86, 91, 93]),
             (89283, "Diana Prince", [95, 81, 72, 100, 87, 93, 97, 84, 91, 93]),
             (62755, "Carol Danvers", [87, 92, 95, 100, 81, 98, 99, 83, 87, 100]),
             (12897, "Bruce Banner", [100, 99, 98, 99, 100, 92, 100, 97, 99, 98]),
             (33744, "Billy Batson", [75, 71, 78, 74, 79, 84, 77, 79, 72, 88]),
             (11926, "Peter Parker", [98, 100, 97, 99, 100, 95, 100, 97, 100, 99]),
             (45617, "Janet Van Dyke", [77, 72, 74, 71, 88, 82, 81, 79, 85, 76]),
             (99914, "Tony Stark", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]),
             (52267, "Matt Murdock", [76, 81, 89, 95, 86, 93, 77, 95, 99, 74]),
             (10082, "Steve Rogers", [95, 95, 95, 98, 92, 98, 96, 99, 97, 92]),
             (53666, "Wade Wilson", [52, 56, 41, 64, 71, 83, 33, 59, 37, 77])]

    GoTList = [(121212, "Olenna Tyrell", [95, 95, 95, 98, 92, 98, 96, 99, 97, 92]),
             (987965, "Tyrion Lannister", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]),
             (475920, "Greyworm", [100, 98, 99, 100, 97, 89, 95, 100, 99, 100]),
             (273596, "Sansa Stark", [100, 100, 100, 100, 100, 100, 100, 100, 98, 100]),
             (355446, "Brienne of Tarth", [86, 83, 92, 81, 87, 95, 84, 75, 96, 91]),
             (779023, "Sandor Clegane", [52, 56, 41, 64, 71, 83, 33, 59, 37, 77]),
             (603475, "Poderick Payne", [95, 81, 72, 100, 87, 93, 97, 84, 91, 93]),
             (553322, "Jamie Lannister", [55, 76, 84, 43, 67, 48, 72, 85, 66, 58]),
             (854374, "Arya Stark", [77, 72, 74, 71, 88, 82, 81, 79, 85, 76]),
             (885910, "Hodor", [98, 100, 97, 99, 100, 95, 100, 97, 100, 99]),
             (658200, "Varys", [100, 99, 98, 99, 100, 92, 100, 97, 99, 98]),
             (115738, "Robb Stark", [75, 71, 78, 74, 79, 84, 77, 79, 72, 88]),
             (228301, "Petyr Baelish", [98, 100, 97, 99, 100, 95, 100, 97, 100, 99]),
             (116387, "Tormund Giantsbane", [77, 72, 74, 71, 88, 82, 81, 79, 85, 76]),
             (371157, "Cersei Lannister", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]),
             (692046, "Jon Snow", [76, 81, 89, 95, 86, 93, 77, 95, 99, 74]),
             (475001, "Eddard Stark", [95, 95, 95, 98, 92, 98, 96, 99, 97, 92]),
             (729463, "Gendry Waters", [78, 63, 82, 55, 88, 76, 72, 79, 85, 73])]

    HPList = [(5432, "Tom M. Riddle", [86, 83, 92, 81, 87, 95, 84, 75, 96, 91]),
             (3746, "Draco Malfoy", [100, 88, 96, 92, 95, 81, 77, 93, 100, 85]),
             (1526, "Ginny Weasley", [95, 81, 72, 100, 87, 93, 97, 84, 91, 93]),
             (5904, "Hermione Granger", [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]),
             (4113, "Ron Weasley", [77, 72, 74, 71, 88, 82, 81, 79, 85, 76]),
             (7640, "Harry Potter", [76, 81, 89, 95, 86, 93, 77, 95, 99, 74]),
             (2205, "Rubeus Hagrid", [75, 68, 78, 74, 79, 84, 77, 79, 72, 88]),
             (6229, "Albus Dumbledore", [98, 100, 97, 99, 100, 95, 100, 97, 100, 99]),
             (7777, "Luna Lovegood", [98, 100, 97, 99, 100, 95, 100, 97, 100, 99]),
             (1697, "Severus Snape", [100, 99, 98, 99, 100, 92, 100, 97, 99, 98]),
             (4731, "Dolores Umbridge", [95, 95, 95, 98, 92, 98, 96, 99, 97, 92]),
             (1084, "Minerva McGonagall", [95, 91, 98, 94, 99, 84, 87, 89, 92, 88]),
             (2988, "Neville Longbottom", [77, 72, 74, 71, 88, 82, 81, 79, 85, 76]),
             (4432, "Sirius Black", [78, 63, 82, 55, 88, 76, 72, 79, 85, 73]),
             (6135, "Bellatrix Lestrange", [55, 76, 84, 43, 67, 48, 72, 85, 66, 58])]

    
    # List of Student Lists
    allLists = [SHList, GoTList, HPList]

    # Loop to run through lists and perform necessary actions
    for i in range (0, (len(allLists))):
        # initialize root and tmp nodes
        root = None
        student = None
        # Print unsorted list
        print("\n\n\n---Unsorted List ", i, "---")
        print(allLists[i])

        # Build BST from List
        for j in range(0, len(allLists[i])):
            nNode = Node(j, allLists[i][j][0])
            root = insertNode(root, nNode)

        # Print in order traversal
        print("\n---In Order Traversal---")
        trav(root, allLists[i])

        # Switch depending on which list
        # Superhero list (i = 0)
        if(i == 0):
            print("\n---Search---")
            # Search for student
            student = find(root, 33744)
            print("Found student", student.val[1], ":", SHList[student.val[0]])

            student = find(root, 53666)
            print("Found student", student.val[1], ":", SHList[student.val[0]])

            # Delete records
            print("\n---Delete---")
            print("Remove 'Matt Murdock'")
            root = delNode(root, 52267)

            print("---In Order Traversal After Delete---")
            trav(root, SHList)

            print("\nRemove 'Carol Danvers'")
            root = delNode(root, 62755)

            print("---In Order Traversal After Delete---")
            trav(root, SHList)

            # Insert new record to list
            SHList.append((25252, "Ororo Munroe", [82, 97, 93, 85, 100, 47, 76, 84, 95, 88]))

            # Insert new record to BST
            newI = (len(SHList)-1)
            tmpNode = Node(newI, SHList[newI][0])
            root = insertNode(root, tmpNode)
        # GoT List (i = 1)
        elif(i == 1):
            print("\n---Search---")
            # Search for student
            student = find(root, 854374)
            print("Found student", student.val[1], ":", GoTList[student.val[0]])

            student = find(root, 729463)
            print("Found student", student.val[1], ":", GoTList[student.val[0]])

            # Delete record
            print("\n---Delete---")
            print("Remove 'Olenna Tyrell'")
            root = delNode(root, 121212)

            print("---In Order Traversal After Delete---")
            trav(root, GoTList)

            print("\nRemove 'Petyr Baelish'")
            root = delNode(root, 228301)

            print("---In Order Traversal After Delete---")
            trav(root, GoTList)
            
            # Insert new record to list
            GoTList.append((339701, "Daenerys Targaryen", [82, 97, 93, 85, 100, 47, 76, 84, 95, 88]))

            # Insert new record to BST
            newI = (len(GoTList)-1)
            tmpNode = Node(newI, GoTList[newI][0])
            root = insertNode(root, tmpNode)
        # HP List (i = 2)
        elif(i == 2):
            print("\n---Search---")
            # Search for student
            student = find(root, 1526)
            print("Found student", student.val[1], ":", HPList[student.val[0]])

            student = find(root, 7640)
            print("Found student", student.val[1], ":", HPList[student.val[0]])

            # Delete record
            print("\n---Delete---")
            print("Remove 'Dolores Umbridge'")
            root = delNode(root, 4731)

            print("---In Order Traversal After Delete---")
            trav(root, HPList)

            print("\nRemove 'Tom M. Riddle'")
            root = delNode(root, 5432)

            print("---In Order Traversal After Delete---")
            trav(root, HPList)
            
            # Insert new record to list
            HPList.append((6296, "Newt Scamander", [95, 81, 96, 100, 87, 93, 97, 84, 91, 93]))

            # Insert new record to BST
            newI = (len(HPList)-1)
            tmpNode = Node(newI, HPList[newI][0])
            root = insertNode(root, tmpNode)

        # Print unsorted list after adding new record
        print("\n---Unsorted List After Addition---")
        print(allLists[i])

        # Print BST after adding new record
        print("\n---In Order Traversal After Addition")
        trav(root, allLists[i])

main()
