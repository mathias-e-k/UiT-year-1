from Dijkstra_adjacency_matrix import WeightedGraph 
        
def create_adjacency_matrix(edges):
    size = max(edges, key=lambda i: i[0])[0] + 1
    adjacency_matrix = [[None] * size for _ in range(size)]
    for edge in edges:
        x, y, w = edge
        adjacency_matrix[x][y] = w
    return adjacency_matrix  

# Create vertices
vertices = ["Seattle", "San Francisco", "Los Angeles",
      "Denver", "Kansas City", "Chicago", "Boston", "New York",
      "Atlanta", "Miami", "Dallas", "Houston"]

# Create edges
edges = [
      [0, 1, 807], [0, 3, 1331], [0, 5, 2097],
      [1, 0, 807], [1, 2, 381], [1, 3, 1267],
      [2, 1, 381], [2, 3, 1015], [2, 4, 1663], [2, 10, 1435],
      [3, 0, 1331], [3, 1, 1267], [3, 2, 1015], [3, 4, 599], 
      [3, 5, 1003],
      [4, 2, 1663], [4, 3, 599], [4, 5, 533], [4, 7, 1260],
      [4, 8, 864], [4, 10, 496],
      [5, 0, 2097], [5, 3, 1003], [5, 4, 533], 
      [5, 6, 983], [5, 7, 787],
      [6, 5, 983], [6, 7, 214],
      [7, 4, 1260], [7, 5, 787], [7, 6, 214], [7, 8, 888],
      [8, 4, 864], [8, 7, 888], [8, 9, 661], 
      [8, 10, 781], [8, 11, 810],
      [9, 8, 661], [9, 11, 1187],
      [10, 2, 1435], [10, 4, 496], [10, 8, 781], [10, 11, 239],
      [11, 8, 810], [11, 9, 1187], [11, 10, 239]
    ]

adjacency_matrix = create_adjacency_matrix(edges)
# Create a graph
graph1 = WeightedGraph(vertices, adjacency_matrix)
print("Adjacency Matrix:")
graph1.print_adjacency_matrix()

# Obtain a shortest path
tree1 = graph1.getShortestPath(5) # Get shortest path from index 5
tree1.printAllPaths()

# Display shortest paths from Houston to Chicago
print("Shortest path from Houston to Chicago: ")
path = tree1.getPath(11)
print(path)

# Create vertices and edges
vertices = [x for x in range(5)]
adjacency_matrix = [[None, 2, None, 8, None],
                    [2, None, 7, 3, None],
                    [None, 7, None, 4, 5],
                    [8, 3, 4, None, 6],
                    [None, None, 5, 6, None]]

# Create a graph
graph2 = WeightedGraph(vertices, adjacency_matrix)
print("Adjacency Matrix:")
graph2.print_adjacency_matrix()

# Obtain a shortest path
tree2 = graph2.getShortestPath(3)
tree2.printAllPaths()