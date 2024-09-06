# This program does not always produce an optimal solution
# Example: 6 3 3 2 2 2 2
# This program: [6 3] [3 2 2 2] [2]
# Optimal solution: [6 2 2] [3 3 2 2]


class Bin:  
    def __init__(self, maxWeight = 10):
        self.maxWeight = maxWeight
        self.totalWeight = 0
        self.objects = []

    def addItem(self, weight):
        if self.totalWeight + weight <= self.maxWeight:
            self.objects.append(weight)
            self.totalWeight += weight
            return True
        else:
            return False

    def getNumberOfObjects(self):
        return len(self.objects)

    def __str__(self):
        output = ""        
        for e in self.objects:
            output += str(e) + " "

        return output

if __name__ == "__main__":
    bins = []
    user_input = input("Enter the weight of the objects: ").split(" ")
    objects = [int(x) for x in user_input if int(x) <= 10]
    objects.sort(reverse=True)
    sum = 0

    for object in objects:
        sum += int(object)
        object_in_bin = False

        for bin in bins:
            if bin.addItem(int(object)):
                object_in_bin = True
                break

        if not object_in_bin:
            # Create a new bin if the object doesn't fit into any previous bins
            bins.append(Bin())
            bins[-1].addItem(int(object))
            object_in_bin = True


    for i, bin in enumerate(bins):
        print(f"Container {i+1} contains objects with weight", end=" ")
        print(bin)
    print(f"Packed {len(objects)} objects with a total weight of {sum} into {len(bins)} {'bins' if len(bins) > 1 else 'bin'}.")
            
