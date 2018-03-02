#-*- coding: utf-8 -*-
# Bellman-Ford algorithm is straightforward algorithm of finding shortest path
# time complexity is O(VE) when V is #vertices and E is #edges

INF = 987654321
d = None
path = None

class Edge:

    def __init__(self, frm, to, weight):
        self.frm = frm
        self.to = to
        self.weight = weight


def relax(edge):
    if d[edge.to] > d[edge.frm] + edge.weight:
        d[edge.to] = d[edge.frm] + edge.weight
        # parent edge를 저장
        path[edge.to] = edge.frm


def bellman_ford(adj, s, e):
    # 그래프의 연관배열 adj를 기준으로 s에서 e로의 최단경로를 구하는 함수
    d[s] = 0
    for vertex in adj:
        for edge in vertex:
            relax(edge)
    # relaxation 후 각 edge를 조사하여 negative cycle여부 조사
    for vertex in adj:
        for edge in vertex:
            # negative cycle이 없을 경우 relaxation 이후 아래 조건을 만족하는 edge가 없어야함
            if d[edge.to] > d[edge.frm] + edge.weight:
                print('negative cycle')
                return ''
    # path가 parent edge를 저장하기 때문에 그 순서를 뒤집으면 s에서 e로의 최단경로가 된다
    ret = []
    cursor = path[e]
    while cursor:
        ret.append(cursor)
        cursor = path[cursor]
    ret.append(s)
    reversed(ret)
    return ret


def main():
    V = [x for x in range(7)]
    testcases = [
        [ # no negative cycle
          # [from, to, weight]
            [0, 1, 1], [0, 2, 2],
            [1, 2, 3], [1, 3, 5],
            [1, 5, 2], [2, 1, 1],
            [2, 4, 1], [3, 5, 3],
            [4, 3, 2], [4, 6, 1],
            [5, 4, 1], [5, 6, 4]
        ],
        [ # negative cycle
            [0, 1, 2], [0, 2, 4],
            [2, 4, -6], [3, 2, 3],
            [3, 5, -2], [4, 3, 2],
            [4, 5, 1], [5, 6, 10]
        ]
    ]
    for tc in testcases:
        global INF, d, path
        d = [INF for _ in V]
        path = [None for _ in V]
        adj = [[] for _ in V]
        for e in tc:
            edge = Edge(e[0], e[1], e[2]) # from, to, weight
            adj[edge.frm].append(edge)
        print(bellman_ford(adj, 0, 6))


if __name__ == "__main__":
    main()

