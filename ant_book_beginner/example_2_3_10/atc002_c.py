from heapq import heappop, heappush, heapify

class MeldableHeap():
    def __init__(self):
        self.heap = []

    def top(self):
        return self.heap[0]

    def pop(self):
        return heappop(self.heap)

    def push(self, x):
        heappush(self.heap, x)

    def meld(self, other):
        if len(self.heap) < len(other.heap):
            self.heap, other.heap = other.heap, self.heap
        while other.heap:
            self.push(other.heap.pop())

INF = (1 << 32) - 1

def hu_tucker(n, arr):
    w = list(arr)
    lt = [0] * n
    rt = [0] * n
    cost = [0] * (n - 1)
    heap = [MeldableHeap() for _ in range(n - 1)]
    queue = []
    for i in range(n - 1):
        lt[i] = i - 1
        rt[i] = i + 1
        cost[i] = w[i] + w[i + 1]
        queue.append(cost[i] * n + i)
    heapify(queue)
    res = 0
    for _ in range(n - 1):
        while True:
            p = heappop(queue)
            c, i = divmod(p, n)
            if cost[i] == c and rt[i] >= 0: break
        ml = mr = False
        if heap[i].heap and w[i] + heap[i].top() == c:
            heap[i].pop()
            ml = True
        elif w[i] + w[rt[i]] == c:
            ml = mr = True
        else:
            top = heap[i].pop()
            if heap[i].heap and heap[i].top() + top == c:
                heap[i].pop()
            else:
                mr = True
        res += c
        heap[i].push(c)
        if ml: w[i] = INF
        if mr: w[rt[i]] = INF
        if ml and i > 0:
            j = lt[i]
            heap[j].meld(heap[i])
            rt[j] = rt[i]
            rt[i] = -1
            lt[rt[j]] = j
            i = j
        if mr and rt[i] + 1 < n:
            j = rt[i]
            heap[i].meld(heap[j])
            rt[i] = rt[j]
            rt[j] = -1
            lt[rt[i]] = i
        cost[i] = w[i] + w[rt[i]]
        if heap[i].heap:
            top = heap[i].pop()
            cost[i] = min(cost[i], w[i] + top, w[rt[i]] + top)
            if heap[i].heap: cost[i] = min(cost[i], heap[i].top() + top)
            heap[i].push(top)
        heappush(queue, cost[i] * n + i)
    return res

import sys
input = sys.stdin.buffer.readline

print(hu_tucker(int(input()), map(int, input().split())))
