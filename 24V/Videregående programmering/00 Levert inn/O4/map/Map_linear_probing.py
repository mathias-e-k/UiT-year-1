# Define the default hash-table size
DEFAULT_INITIAL_CAPACITY = 4
  
# Define default load factor
DEFAULT_MAX_LOAD_FACTOR = 0.75 
     
# Define the maximum hash-table size to be 2 ** 30
MAXIMUM_CAPACITY = 2 ** 30 
  
class Map:
    def __init__(self, capacity = DEFAULT_INITIAL_CAPACITY, 
                 loadFactorThreshold = DEFAULT_MAX_LOAD_FACTOR):
        # Current hash-table capacity. Capacity is a power of 2
        self.capacity = capacity

        # Specify a load factor used in the hash table
        self.loadFactorThreshold = loadFactorThreshold
   
        # Create a list of empty buckets
        self.table = []
        for i in range(self.capacity):
            self.table.append(None) # Use open addressing
        
        self.size = 0 # Initialize map size

    # Add an entry (key, value) into the map 
    def put(self, key, value):
        if self.size >= self.capacity * self.loadFactorThreshold:          
            if self.capacity == MAXIMUM_CAPACITY:
                raise RuntimeError("Exceeding maximum capacity")
      
            self.rehash()

        # Use open addressing
        i = self.getHash(hash(key))
        while self.table[i] != None and self.table[i][0] != None:
            i = (i + 1) % self.capacity

        # Add an entry (key, value) to hashTable[index]
        self.table[i] = ([key, value])

        self.size += 1 # Increase size
 
    # Remove the entry for the specified key 
    def remove(self, key):
        i = self.getHash(hash(key))

        # Use open addressing
        while self.table[i] != None and (self.table[i][0] == None or self.table[i][0] != key):
            i = (i + 1) % self.capacity
      
        # Remove the first entry that matches the key from a bucket
        if self.table[i] != None and self.table[i][0] == key:
            # A special marker entry (None, None) is placed for the deleted entry
            self.table[i] = (None, None)
            self.size -= 1

    # Return true if the specified key is in the map
    def containsKey(self, key):
        if self.get(key) != None:
            return True
        return False
  
    # Return true if this map contains the specified value 
    def containsValue(self, value):
        for i in range(self.capacity):
            if self.table[i] is None:
                continue
            if self.table[i][1] == value:
                return True
        return False
  
    # Return a set of entries in the map 
    def items(self):
        entries = []
    
        for i in range(self.capacity):
            if self.table[i] != None:
                entries.append(self.table[i]) # For open addressing
                
        return tuple(entries)
    
    # Return the first value that matches the specified key 
    def get(self, key):
        i = self.getHash(hash(key))
        while self.table[i] != None:
            if self.table[i][0] != None and self.table[i][0] == key:
                return self.table[i][1]
            i = (i + 1) % self.capacity
                
        return None
  
    # Return all values for the specified key in this map
    def getAll(self, key):
        values = []
        i = self.getHash(hash(key))

        while self.table[i] != None:
            if self.table[i][0] != None and self.table[i][0] == key:
                values.append(self.table[i][1])
            i = (i + 1) % self.capacity
            
        return tuple(values)
  
    # Return a set consisting of the keys in this map
    def keys(self):
        keys = []
    
        for i in range(0, self.capacity):
            if self.table[i] != None:
                keys.append(self.table[i][0])
    
        return keys
  
    # Return a set consisting of the values in this map 
    def values(self):
        values = []
    
        for i in range(self.capacity):
            if self.table[i] != None: 
                values.append(self.table[i][1])
        
        return values
                  
    # Remove all of the entries from this map 
    def clear(self):
        self.size = 0 # Reset map size
        
        self.table = [] # Reset map
        for i in range(self.capacity):
            self.table.append(None)

    # Return the number of mappings in this map 
    def getSize(self):
        return self.size
        
    # Return true if this map contains no entries 
    def isEmpty(self):
        return self.size == 0
    
    # Rehash the map 
    def rehash(self):
        temp = self.items() # Get entries
        self.capacity *= 2 # Double capacity    
        self.table = [] # Create a new hash table
        self.size = 0 # Clear size
        for i in range(self.capacity):
            self.table.append(None)
            
        for entry in temp:
            self.put(entry[0], entry[1]) # Store to new table

    # Return the entries as a string 
    def toString(self):
        return str(self.items())
    
    # Return a string representation for this map 
    def setLoadFactorThreshold(self, threshold):
        self.loadFactorThreshold = threshold

    # Return the hash table as a string 
    def getTable(self):
        return str(self.table)
    
    def supplementalHash(self, h):
        h ^= (h >> 20) ^ (h >> 12)
        return h ^ (h >> 7) ^ (h >> 4)

    def getHash(self, hashCode):
        return self.supplementalHash(hashCode) & (self.capacity - 1)