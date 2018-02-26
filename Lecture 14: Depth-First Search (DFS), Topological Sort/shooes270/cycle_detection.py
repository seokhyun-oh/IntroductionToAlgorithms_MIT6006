parent = None


def has_cycle(V, adj):
    global parent
    parent = {}
    fin = []
    cycle = False
    for v in V:
        if v not in parent and not cycle:
            parent[v] = None
            cycle |= dfs_visit(adj, v, fin)
    return cycle


def dfs_visit(adj, v, fin):
    cycle = False
    for u in adj[v]:
        if u not in parent and not cycle:
            parent[u] = v
            cycle |= dfs_visit(adj, u, fin)
        elif u not in fin:
            # 이미 지나온 점이지만 종료되지 않고 edge의 종점으로 존재할 경우 : 사이클
            return True
    fin.append(v)
    return cycle


def main():
    V = [0, 1, 2, 3, 4, 5]
    testcases = [
        [
            [0, 1], [0, 3],
            [1, 4], [2, 4], [2, 5],
            [3, 1], [4, 3], [5, 5]
        ],
        [
            [0, 1], [0, 3], [1, 4],
            [2, 4], [2, 5], [4, 3]
        ]
    ]

    for tc in testcases:
        adj = [[] for _ in range(len(V))]
        for edge in tc:
            adj[edge[0]].append(edge[1])
        print(has_cycle(V, adj))


if __name__ == "__main__":
    main()
