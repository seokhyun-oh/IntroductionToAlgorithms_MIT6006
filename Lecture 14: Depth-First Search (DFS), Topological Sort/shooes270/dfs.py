def dfs(V, adj):
    parent = {}
    L = []
    for v in V:
        if v not in parent:
            parent[v] = None
            dfs_visit(adj, v, L, parent)
    return L


def dfs_visit(adj, v, L, parent={}):
    for u in adj[v]:
        if u not in parent:
            parent[u] = v
            dfs_visit(adj, u, L, parent)
    L.append(v)


def main():
    V = [0, 1, 2, 3, 4, 5]
    edges = [
        [0, 1], [0, 3],
        [1, 4], [2, 4], [2, 5],
        [3, 1], [4, 3], [5, 5]
    ]
    adj = [[] for _ in range(len(V))]
    for edge in edges:
        # 유향그래프이므로 단방향으로 표현합니다.
        adj[edge[0]].append(edge[1])
    print(dfs(V, adj))


if __name__ == "__main__":
    main()
