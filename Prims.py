INF = 99999

def getMatrix(size):
    return [[0]*size for _ in range(size)]

def displayMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    print()

def addEdge(matrix, src, dest, weight):
    matrix[src][dest] = matrix[dest][src] = weight

def prims(matrix, start):
    global INF
    size = len(matrix)
    visited = [False]*size
    parent = [-1]*size
    weight = [INF]*size

    output = []
    weight[start] = 0
    parent[start] = start
    visited[start] = True
    curr = start
    while len(output) < (size-1):
        for i in range(size):
            if matrix[curr][i] > 0:
                if visited[i] == False:
                    if weight[i] > matrix[curr][i]:
                        weight[i] = matrix[curr][i]
                        parent[i] = curr
        curr = findMin(visited, weight)
        visited[curr] = True
        output.append([parent[curr],curr ,weight[curr]])
    return output

def findMin(visited, weight):
    global INF
    min = -1
    minweight = INF
    for i in range(len(visited)):
        if not visited[i]:
            if minweight > weight[i]:
                min = i
                minweight = weight[i]
    return min




size = int(input("Enter number of vertices : "))
edges = int(input("Enter number of edges : "))
print("Enter src dest weight : ")
matrix = getMatrix(size)
for i in range(edges):
    src, dest, weight = map(int, input().split())
    addEdge(matrix, src, dest, weight)

op = prims(matrix, 0)

print("Minimum spanning tree : ")
for i in op:
    print(f"{i[0]} {i[1]} : {i[2]}")



# 4
# 5
# addEdge(matrix, 0, 1, 2)
# addEdge(matrix, 0, 2, 4)
# addEdge(matrix, 1, 2, 1)
# addEdge(matrix, 1, 3, 4)
# addEdge(matrix, 2, 3, 6)

# 5
# 7
# addEdge(matrix, 0, 1, 2 )
# addEdge(matrix, 0, 3, 6)
# addEdge(matrix, 1, 2, 3)
# addEdge(matrix, 1, 3, 8)
# addEdge(matrix, 1, 4, 5)
# addEdge(matrix, 2, 4, 7)
# addEdge(matrix, 3, 4, 9)