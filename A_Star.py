class Node:
    def __init__(self, puzzle, level, locked, fval):
        self.puzzle = puzzle
        self. level = level
        self.fval = fval
        self.locked = locked
        self.size = len(self.puzzle)
    
    def find(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == -1:
                    return i, j
    
    def copy(self):
        copymat = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(self.puzzle[i][j])
            copymat.append(temp)
        return copymat

    def generateChild(self):
        x, y = self.find()
        moveList = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        childrens = []
        for move in moveList:
            puzz = self.shuffle(x, y, move[0], move[1])
            if puzz:
                locked = [x, y]
                child = Node(puzz, self.level + 1, locked, 0)
                childrens.append(child)
        return childrens
    
    def shuffle(self, x1, y1, x2, y2):
        xlock = self.locked[0]
        ylock = self.locked[1]
        if x2>= self.size or x2<0 or y2>= self.size or y2<0:
            return None
        if x2 == xlock and y2 == ylock:
            return None
        temp = self.copy()
        temp[x1][y1], temp[x2][y2] =  temp[x2][y2], temp[x1][y1]
        return temp
    
class Puzzle:
    def __init__(self, size):
        self. size = size
        self.open = []
        self.closed = []
    
    def accept(self):
        puzz = []
        for i in range(self.size):
            temp = []
            for j in range(self.size):
                temp.append(int(input()))
            puzz.append(temp)
        return puzz
    
    def f(self, start, goal):
        return self.h(start.puzzle, goal) + start.level
    
    def h(self, start, goal):
        temp = 0
        for i in range(self.size):
            for j in range(self.size):
                if start[i][j] != goal[i][j]:
                    temp+=1
        return temp
    
    def process(self):
        print("Start Input : ")
        start = self.accept()
        print("\nGoal Input : ")
        goal = self.accept()
        start = Node(start, 0, [-1, -1], 0)
        start.fval = self.f(start, goal)

        self.open.append(start)

        while True:
            curr = self.open[0]
            del self.open[0]

            for i in curr.puzzle:
                print(i)
            print("\n")

            if(self.h(curr.puzzle, goal) == 0):
                break

            for i in curr.generateChild():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(curr)

            self.open.sort(key = lambda x:x.fval,reverse=False)


puz = Puzzle(3)
puz.process()

# print(len(puz.closed))

# for i in puz.closed:
#     for j in (i.puzzle):
#         print(j)
#     print()






# start = [[1,2,3],[-1,4,6],[7,5,8]]
# goal = [[1,2,3],[4,5,6],[7,8,-1]]


# start= [[1, 2, 3],[5, 6, -1],[7, 8, 4]]
# goal = [[1, 2, 3],[5, 8, 6],[-1, 7, 4]]


# start= [[1, 2, 3],[8, 6, -1],[7, 5, 4]]
# goal = [[1, 2, 3],[8, -1, 4],[7, 6, 5]]