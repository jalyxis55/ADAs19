# Jennifer Shelby
# Project 8 - Graph Application and BFS
# Spring 2019
# Algorithm Design and Analysis

# Graph Class
class Graph():

    # Constructor
    def __init__(self, v):
        self.vertex = v
        self.graph = [[0 for c in range(v)] for r in range(v)]

    # isCol() boolean function that checks to see if the current color is ok to be used
    # Pre-condition: v - vertex, list of colors - color, current color, c
    # Post-condition: Returns True if the current color can be used and returns
    # False if the color cannot be used
    def isCol(self, v, color, c):
        for i in range(0, 12):
            #print("I: ", i)
            #print("V: ", v)
            if(self.graph[v][i] == 1 and color[i] == c):
                return False
        return True

    # colorUtil() - recursive function that colors the nodes of the map
    # Pre-condition: number of colors to be used - m, array of colors - color, vertex - v
    # Post-condition: sets colors in color array where the index corresponds to the
    # on the map
    def colorUtil(self, x, color, v):
        # Base case
        if(v == self.vertex):
            return True

        for c in range (1, 13):
            if (self.isCol(v, color, c) == True):
                color[v] = c
                if (self.colorUtil(x, color, v+1) == True):
                    return True
                color[v] = 0

    # colorGraph() - Colors the graph
    # Pre-condition: Takes x, the number of available colors
    # Post-condition: Prints the color array. The index of the array corresponds to the country
    # the value corresponds to the color used to color that vertex
    def colorGraph(self, x):
        color = [0] * self.vertex

        if(self.colorUtil(x, color, 0) == False):
            return False

        # Print solution
        print("Solution for South America: ")
        for c in color:
            print(c)
        return True

# Driver function
def main():
    # Color Dictionary
    #colorDict = {0: "Blue", 1: "Brown", 2: "Green", 3: "Lavender", 4: "Orange", 5: "Pink", 6: "Red", 7: "Yellow", 8: "Violet", 9: "Gold", 10: "Gray", 11: "Indigo", 12: "Silver"}
    # Country Dictionary
    #countryDict = {0: "Brazil", 1: "French", 2: "Suriname", 3: "Guyana", 4: "Venezuela", 5: "Columbia", 6: "Peru", 7: "Ecuador", 8: "Bolivia", 9: "Paraguay", 10: "Argentina", 11: "Uruguay", 12: "Chile"}
    # Graph
    g = Graph(13)
    # Populate graph with adjacent nodes
    #g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
    g.graph = [[0,1,1,1,1,1,1,0,1,1,1,1,0], [1,0,1,0,0,0,0,0,0,0,0,0,0], [1,1,0,1,0,0,0,0,0,0,0,0,0], [1,0,1,0,1,0,0,0,0,0,0,0,0], [1,0,0,1,0,1,0,0,0,0,0,0,0], [1,0,0,0,1,0,1,1,0,0,0,0,0], [1,0,0,0,0,1,0,1,1,0,0,0,1], [0,0,0,0,0,1,1,0,0,0,0,0,0], [1,0,0,0,0,0,1,0,0,1,1,0,1], [1,0,0,0,0,0,0,0,1,0,1,0,0], [1,0,0,0,0,0,0,0,1.1,0,1,1], [1,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,1,0,1,0,1,0,0]]
    # Number of colors available 
    numColors = 13
    g.colorGraph(numColors)
    

main()
    
