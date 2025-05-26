## BFS 개념 코드
## Queue를 이용
from collections import deque

N = 5    # 노드의 수

adj_list = [[] for _ in range(N)]
visited = [False] * N


# Create Adjacency List
adj_list[0].append(1)
adj_list[0].append(2)
adj_list[1].append(4)
adj_list[1].append(3)
adj_list[2].append(3)
adj_list[3].append(0)

# Excute Breadth-First search with start node '0'
q = deque()
q.append(0)
visited[0] = True

while q:
    node = q.popleft()
    print(node, end=" ")

    for adj_node in adj_list[node]:
        if visited[adj_node]:
            continue

        q.append(adj_node)
        visited[adj_node] = True
