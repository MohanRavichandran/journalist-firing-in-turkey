import numpy

def transmit(x, n):
    return [x+2**m for m in range(n) if x+2**m < 2**n] + [x-2**m for m in range(n) if x-2**m >= 0]


def algo(vertexset,counter):
    if counter == 0:
        return [0]
    elif counter == 1:
            return [2**n-1]
    else:
         return [numpy.random.randint(2**n-1)]
        



#print "Round number:", counter, "Vertices reached", vertexset

n = 11


iteration = 0
answer = []

while iteration < 100:
    
    counter = 0
    vertexset = []
    vertexset = vertexset + algo(vertexset,counter)
   
    while len(vertexset)<2**n:
        counter = counter + 1
        vertexsetnew = []
        for entry in vertexset:
            vertexsetnew = vertexsetnew + transmit(entry,n)
        vertexset = vertexset + vertexsetnew
        vertexset = list(set(vertexset))
        
        vertexset = vertexset+algo(vertexset,counter)
    answer = answer + [counter] 
    print counter
    iteration = iteration + 1
        #print "Round number:", counter, "Vertices reached", vertexset

print answer
        