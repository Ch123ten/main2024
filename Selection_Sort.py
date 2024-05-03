def selectionSort(list):
    size = len(list)
    for i in range(size-1):
        small = i
        for j in range(i+1, size):
            if list[small] > list[j]:
                small = j
        list[i], list[small] = list[small], list[i]
    return list

INF = 99999

def inputList():
    list = []
    size = int(input("Enter the size of list : "))
    for i in range(size):
        list.append(int(input("Enter the number : ")))
    return list
    
def printList(list):
    for i in list:
        print(i, end=' ')


list = inputList()
print("Before Sorting : ")
printList(list)
print("\nAfter Sorting : ")
list = selectionSort(list)
printList(list)
print()