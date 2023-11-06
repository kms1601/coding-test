from collections import deque
from time import time
import random

def draw(list):
    for i in list:
        print(i * '*')

def heapsort(list):
    result = []
    heap = deque()

    for index in range(len(list)):
        heap.append(list[index])
        while index > 0:
            if heap[index] < heap[(index - 1)// 2]:
                heap[index], heap[(index - 1)// 2] = heap[(index - 1)// 2], heap[index]
                index = (index - 1)// 2
            else: break
    
    while True:
        result.append(heap.popleft())
        if not heap: break
        index = 0
        heap.appendleft(heap.pop())
        while True:
            if index * 2 + 2 < len(heap):
                if heap[index * 2 + 1] < heap[index * 2 + 2]:
                    heap[index], heap[index * 2 + 1] = heap[index * 2 + 1], heap[index]
                    index = index * 2 + 1
                else:
                    heap[index], heap[index * 2 + 2] = heap[index * 2 + 2], heap[index]
                    index = index * 2 + 2
            elif index * 2 + 1 < len(heap) and heap[index * 2 + 1] < heap[index]:
                heap[index], heap[index * 2 + 1] = heap[index * 2 + 1], heap[index]
                index = index * 2 + 1
            else: break
    return result
             
        
    

list = [i for i in range(1, 11)]
list = random.sample(list, len(list))
draw(list)
time1 = time()
print(heapsort(list))
time2 = time()
print(time2 - time1)