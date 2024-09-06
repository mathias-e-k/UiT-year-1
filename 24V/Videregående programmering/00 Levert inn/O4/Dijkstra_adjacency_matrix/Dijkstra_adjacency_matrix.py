from Tree import Tree

INFINITY = 1e+308 # Infinity value

class WeightedGraph:
    def __init__(self, vertices, adjacency_matrix):
        self.vertices = vertices
        self.adjacency_matrix = adjacency_matrix
        self.neighbors = self.get_neighbour_lists()

    def print_adjacency_matrix(self):
        print("[", end="")
        for line in self.adjacency_matrix[:-1]:
            print(line, end=",\n")
        print(self.adjacency_matrix[-1], end="]\n")

    # Override this method in the Graph class
    def get_neighbour_lists(self):
        self.neighbors = []
        for i in range(len(self.vertices)):
            self.neighbors.append([]) # Each element is another list
            
        for i, line in enumerate(self.adjacency_matrix):
            for j, weight in enumerate(line):
                # Insert a neigbour v
                if weight is not None:
                    self.neighbors[i].append(j) 

        return self.neighbors
    
    #Display edges with weights 
    def printWeightedEdges(self):
        for i in range(len(self.neighbors)):
            print(str(self.getVertex(i)) + " (" + str(i), end = "): ")
            for v in self.neighbors[i]:
                print("(" + str(i) + ", " + str(v) + ", "  + str(self.adjacency_matrix[i][v]), end = ") ")
            print()

    # Return the weight between two vertices
    def getWeight(self, u, v):
        return self.adjacency_matrix[u][v]
    
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list
            for line in self.adjacency_matrix:
                line.append(None)
            self.adjacency_matrix.append([None] * len(self.vertices))

    # Override the addEdge method to add a weighted edge 
    def addEdge(self, u, v, w):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v, w) to the graph
            self.neighbors[indexU].append(indexV)
            self.adjacency_matrix[u][v] = w

    # Return the number of vertices in the graph 
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex 
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index 
    def getNeighbors(self, index):
        return self.neighbors[index]
    
    # Return the degree for a specified vertex 
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges 
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " + 
                      str(self.neighbors[u][j]), end = ") ")
            print()

    # Clear graph 
    def clear(self):
        self.vertices = []
        self.neighbors = []
        self.adjacency_matrix = []

    # Find single source shortest paths 
    def getShortestPath(self, sourceVertex):
        cost = self.getSize() * [INFINITY] 
        cost[sourceVertex] = 0 
        parent = self.getSize() * [-1] 
        searched_vertices = []
    
        while len(searched_vertices) < self.getSize():
            current = -1 
            currentMinCost = INFINITY
            for i in range(self.getSize()):
                if i not in searched_vertices and cost[i] < currentMinCost:
                    currentMinCost = cost[i]
                    current = i

            if current == -1:
                break
            else:
                searched_vertices.append(current) 
      
            for neighbour in self.neighbors[current]:
                if neighbour not in searched_vertices and cost[neighbour] > cost[current] + self.adjacency_matrix[current][neighbour]:
                    cost[neighbour] = cost[current] + self.adjacency_matrix[current][neighbour]
                    parent[neighbour] = current 

        return ShortestPathTree(sourceVertex, parent, searched_vertices, cost, self.vertices)

# ShortestPathTree is an inner class in WeightedGraph 
class ShortestPathTree(Tree):
    def __init__(self, sourceIndex, parent, T, costs, vertices):
        super().__init__(sourceIndex, parent, T, vertices)
        self.costs = costs

    # Return the cost for a path from the root to vertex v 
    def getCost(self, v):
        return self.costs[v]

    # Print paths from all vertices to the source 
    def printAllPaths(self):
        print("All shortest paths from " 
            + str(self.vertices[self.root]) + " are:")
        for i in range(len(self.costs)):
            self.printPath(i) # Print a path from i to the source
            print("(cost: " + str(self.costs[i]) + ")") # Path cost