# Line 10
T = []
isInT = [False] * self.getSize() # changed and/or extra

# Line 13
while len(T) < self.getSize():
while not all(b for b in isInT): # changed and/or extra

# Line 19
if i not in T and cost[i] < currentMinCost:
if not isInT[i] and cost[i] < currentMinCost: # changed and/or extra

# Line 26
T.append(u)
isInT[u] = True # changed and/or extra

# Line 31
if e.v not in T and cost[e.v] > e.weight:
if not isInT[e.v] and cost[e.v] > e.weight: # changed and/or extra

# Line 35
return ShortestPathTree(sourceVertex, parent, T, cost, self.vertices)
return ShortestPathTree(sourceVertex, parent, isInT, cost, self.vertices) # changed and/or extra

# Line 48
T = []
isInT = [False] * self.getSize() # changed and/or extra

# Line 51 
while len(T) < self.getSize():
while not all(b for b in isInT): # changed and/or extra

# Line 58 
if i not in T and cost[i] < currentMinCost:
if not isInT[i] and cost[i] < currentMinCost: # changed and/or extra

# Line 64
T.append(u)
isInT[u] = True # changed and/or extra

# Line 68
if e.v not in T and cost[e.v] > e.weight:
if not isInT[e.v] and cost[e.v] > e.weight: # changed and/or extra

# Line 73
return ShortestPathTree(sourceVertex, parent, T, cost, self.vertices)
return ShortestPathTree(sourceVertex, parent, isInT, cost, self.vertices) # changed and/or extra