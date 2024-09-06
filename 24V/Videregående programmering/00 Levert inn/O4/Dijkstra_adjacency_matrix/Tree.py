# Tree class will be discussed in Section 22.5 
class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root # The root of the tree
        # Store the parent of each vertex in a list
        self.parent = parent 
        # Store the search order in a list
        self.searchOrders = searchOrders 
        self.vertices = vertices # vertices of the graph

    # Return the root of the tree 
    def getRoot(self):
        return self.root

    # Return the parent of vertex v 
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order 
    def getSearchOrders(self):
        return self.searchOrders

    # Return number of vertices found 
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)
    
    # Return the path of vertices from a vertex index to the root 
    def getPath(self, index):
        path = []

        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]

        return path

    # Print a path from the root to vertex v 
    def printPath(self, index):
        path = self.getPath(index)
        print("A path from " + str(self.vertices[self.root]) + " to " 
              + str(self.vertices[index]), end = ": ")
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end = " ")

    # Print the whole tree 
    def printTree(self):
        print("Root is: " + str(self.vertices[self.root]))
        print("Edges: ", end = "")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                # Display an edge
                print("(" + str(self.vertices[self.parent[i]]) 
                      + ", " + str(self.vertices[i]), end = ") ")

        print()
