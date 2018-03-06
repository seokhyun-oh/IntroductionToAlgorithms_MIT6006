#-*- coding: utf-8 -*-

def LEFT(idx):
    return 2*idx + 1

def RIGHT(idx):
    return 2*idx + 2

def PARENT(idx):
    if idx is 0:
        return 0
    return (idx-1) // 2


class BinaryMinHeap:
    """
    거리가 최소가 되게하는 greedy algorithm을 구현하기위한 힙으로
    이동거리가 최소인 vertex를 O(1)의 시간에 찾아준다.
    """
    def __init__(self, items=[], comparator=(lambda item, a, b: item[a] < item[b])):
        self.less = comparator
        self.items = []
        for item in items:
            self.push(item)

    def min_heapify(self, idx):
        left, right = LEFT(idx), RIGHT(idx)
        smallest = idx

        if left < len(self.items) and self.less(self.items, left, smallest):
            smallest = left
        if right < len(self.items) and self.less(self.items, right, smallest):
            smallest = right

        if smallest is not idx:
            self.swap(smallest, idx)
            self.min_heapify(smallest)

        parent = PARENT(idx)
        if parent < len(self.items) and self.less(self.items, idx, parent):
            self.swap(idx, parent)
            self.min_heapify(parent)

    def push(self, item):
        pos = len(self.items)
        self.items.append(item) # self.items[pos] = item
        while pos > 0 and self.less(self.items, pos, PARENT(pos)):
            self.swap(pos, PARENT(pos))
            pos = PARENT(pos)

    def swap(self, a, b):
        temp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = temp

    def empty(self):
        return len(self.items) is 0

    def extract_min(self):
        minimum = self.items[0]
        self.items[0] = self.items[-1]
        if len(self.items) > 0:
            del self.items[-1]
            self.min_heapify(0)
        return minimum


class Vertex:
    INF = 987654321
    def __init__(self, index, dist=None):
        self.index = index
        if dist is None:
            self.dist = self.INF
        else:
            self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

class Graph:

    def __init__(self, directed=True):
        self.directed = directed
        self.vertices = []
        self.adj = []

    def add_vertex(self, index):
        while len(self.vertices) <= index:
            self.vertices.append(None)
            self.adj.append([])
        self.vertices[index] = Vertex(index)

    def add_edge(self, s, e):
        self.adj[s].append(e)
        if not self.directed:
            self.adj[e].append(s)


def dijkstra(G, W, s):
    G.vertices[s].dist = 0 # 시작원소의 최단 이동거리는 0
    S = set() # 이미 경유한 원소들의 집합, 중복연산 방지
    check_point = []
    Q = BinaryMinHeap() # 경유하지 않은 원소들 중 가장 가까운 점을 반환하는 우선순위 큐
    [Q.push(v) for v in G.vertices]
    while not Q.empty():
        u = Q.extract_min()
        if u.index in S: # 경유하지 않은 최단거리 원소를 선택(greedy)
            continue
        S.add(u.index)
        check_point.append(u)
        for v in G.adj[u.index]:
            #relaxation of shortest path algorithm
            V = G.vertices[v]
            if V.dist > u.dist + W[(u.index, V.index)]:
                new_dist = u.dist + W[(u.index, V.index)]
                # 우선순위 큐에서 특정 index를 갖는 원소를 O(n)미만의 시간에 찾을수가 없기때문에
                # 동일 index에 새로운 distance를 갖는 원소를 추가하여 우선순위큐에 저장 O(lgn)
                # 기존에 있던 거리가 더 긴 원소는 이후 중복계산을 방지하는 로직으로 제거된다.
                Q.push(Vertex(V.index, new_dist))
    return check_point


def main():
    data = [
        # from, to, weight
        [0, 1, 10], [0, 2, 3],
        [1, 2, 1], [1, 3, 2],
        [2, 1, 4], [2, 3, 8],
        [2, 4, 2], [3, 4, 7],
        [4, 3, 9]
    ]
    V = [x for x in range(5)]

    G = Graph()
    [G.add_vertex(v) for v in V]
    [G.add_edge(e[0], e[1]) for e in data]
    W = {(e[0], e[1]): e[2] for e in data}

    check_point = dijkstra(G, W, 0)
    for v in check_point:
        print('{0}에서 {1}까지 최단거리 : {2}'.format(0, v.index, v.dist))

if __name__ == "__main__":
    main()

