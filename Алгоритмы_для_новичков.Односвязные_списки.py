# Алгоритмы для новичков. Односвязные списки.
'''
Односвязный список Python — это последовательность узлов информации, где каждый отдельный
узел указывает только на следующий узел.
'''
class Node:
    '''ячейка списка'''
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    '''односвязный список'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head != None:
            c = self.head
            out = "LinkedList [" + str(c.value)

            while c.next != None:
                c = c.next
                out += ", " + str(c.value)

            out += "]"
            return out
        else:
            return "LinkedList []"

    def add(self, n):
        self.length += 1

        if self.head == None:
            self.head = self.tail = Node(n, None)
        else:
            self.tail.next = self.tail = Node(n, None)

    def reverse(self):
        '''разворачивание односвязного списка'''
        pNode = None
        cNode = self.head
        nNode = cNode.next

        self.tail = cNode

        while nNode != None:
            cNode.next = pNode
            pNode = cNode
            cNode = nNode
            nNode = cNode.next

        cNode.next = pNode
        self.head = cNode

        def sort(self):
            swaps = True
            while swaps:
                swaps = False

            for j in range(len(L)-1):
                if L[l] > L[j+1]:
                    swaps = True
                    L[j], L[j+1] = L[j+1], L[j]

L = LinkedList()

L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)

print(L)

L.reverse()

print(L)

input()
