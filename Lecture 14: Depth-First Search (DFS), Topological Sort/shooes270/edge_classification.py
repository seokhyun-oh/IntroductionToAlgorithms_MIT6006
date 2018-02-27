class DFSResult:

    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.end_time = {}
        self.edges = {}
        self.order = []
        self.t = 0


def dfs(V, adj):
    result = DFSResult()
    for v in V:
        if v not in result.parent:
            dfs_visit(v, adj, result)
    return result


def dfs_visit(v, adj, result, parent=None):
    result.t += 1
    result.start_time[v] = result.t
    result.parent[v] = parent
    if parent is not None:
        result.edges[(parent, v)] = 'tree'

    for u in adj[v]:
        if u not in result.parent:
            dfs_visit(u, adj, result, v)
        elif u not in result.end_time:
            result.edges[(v, u)] = 'back'
        elif result.start_time[u] < result.start_time[v]:
            result.edges[(v, u)] = 'forward'
        else:
            result.edges[(v, u)] = 'cross'

    result.t += 1
    result.end_time[v] = result.t
    result.order.append(v)


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
    print(dfs(V, adj).edges)


if __name__ == "__main__":
    main()
