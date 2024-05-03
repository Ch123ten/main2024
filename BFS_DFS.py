class Graph:
    def __init__(self):
        self.adjList = {}
    
    def addEdge(self, src, dest):
        if src not in self.adjList:
            self.adjList[src] = []
        if dest not in self.adjList:
            self.adjList[dest] = []
        self.adjList[src].append(dest)
        self.adjList[dest].append(src)
    
    def printAdjList(self):
        for i, j in self.adjList.items():
            print(i,end=' ')
            print(j)
    
    def dfs(self, curr, visited = None):
        if visited is None:
            visited = set()
        if curr not in visited:
            visited.add(curr)
            print(curr, end=' ')
            for next in self.adjList[curr]:
                self.dfs(next, visited)
    
    def bfs(self, queue, visited = None):
        if visited is None:
            visited = set()
        if queue is None:
            return
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                print(curr,end=' ')
                for next in self.adjList[curr]:
                    if next not in visited:
                        queue.append(next)
                self.bfs(queue, visited)


g = Graph()
v= int(input("Enter number of vertices : "))
e = int(input("Enter number of edges : "))
i=0
while i<e:
    src ,dest = map(int, input("Enter v1, v2 : ").split())
    if src>=v or src<0 or dest>=v or dest<0:
        print("Please enter valid edges")
    else:
        g.addEdge(src, dest)
        i+=1

# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 4)
# g.addEdge(3, 4)
# g.addEdge(3, 5)
# g.addEdge(4, 5)
# g.addEdge(5, 0)
# g.addEdge(5, 1)

print("Adjcent List : ")
g.printAdjList()
print()
print("DFS : ")
start = int(input("Enter start vertex for DFS : "))
g.dfs(start)
print()
start = int(input("Enter start vertex for BFS: "))
g.bfs([start])


#6
#10

