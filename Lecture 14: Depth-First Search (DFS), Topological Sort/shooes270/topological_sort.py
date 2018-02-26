from dfs import dfs_visit
from cycle_detection import has_cycle


def topological_sort(V, adj, indegree):
    # 위상정렬은 사이클이 없는 방향그래프에서 구할 수 있다.
    if has_cycle(V, adj):
        print("Not DAG, it has a cycle")
        return []
    L = []
    for v in V:
        # DAG의 방향성을 거스르지 않고 정점들을 나열하는 알고리즘이며
        # DFS로 구현할 경우 진입차수(indegree)가 0인 정점부터 탐색하면 된다.
        if indegree[v] is 0:
            dfs_visit(adj, v, L)
    # 이후 탐색이 종료된 역순으로 나열하면 방향을 거스르지 않는 정점들의 순서로 정렬된다.
    L.reverse()
    return L


def main():
    V = [x for x in range(9)]
    testcases = [
        [
            [0, 1], [3, 1], [3, 4],
            [4, 5], [5, 6], [7, 4],
            [7, 8], [8, 6], [5, 7] # cycle
        ],
        [
            [0, 1], [3, 1], [3, 4],
            [4, 5], [5, 6], [7, 4],
            [7, 8], [8, 6]
        ]
    ]

    for tc in testcases:
        adj = [[] for _ in V]
        indegree = [0 for _ in V]
        for edge in tc:
            adj[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        print(topological_sort(V, adj, indegree))


if __name__ == '__main__':
    main()
