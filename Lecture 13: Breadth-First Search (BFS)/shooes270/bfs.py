def bfs(adj, s):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        print('level {0} : {1}'.format(i-1, frontier))
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1


def main():
    testcase = [
        [0, 1], [0, 4], [1, 5],
        [2, 5], [2, 3], [2, 6],
        [3, 6], [3, 7], [5, 6], [6, 7]
    ]
    adj = [[] for _ in range(8)]
    for edge in testcase:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    bfs(adj, 1)


if __name__ == '__main__':
    main()
