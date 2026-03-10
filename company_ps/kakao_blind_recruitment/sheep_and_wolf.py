# 양과 늑대 (다시 풀어볼 문제)
# 이 문제는 "현재 위치" 중심 탐색이 아니라
# "방문한 집합 + 지금 갈 수 있는 후보 집합" 중심으로 탐색해야함
# 이 문제의 핵심은 "상태 표현 문제"
# 이 문제를 트리 이동문제로 생각하면 안되고, "영역 확장 게임"으로 생각해야함
# 내 첫번째 풀이는 그리디하게 양부터 먼저 가도록 했지만, 이는 항상 좋은 구조가 아님

# 첫번째 풀이 (잘못된 풀이)
#
# from collections import deque
#
# def solution(info, edges):
#     answer = 0
#     n = len(info)
#     adj_list = [[] for _ in range(n)]
#     visited = [False for _ in range(n)]
#     for i in range(len(edges)):
#         adj_list[edges[i][0]].append(edges[i][1])
#         adj_list[edges[i][1]].append(edges[i][0])
#
#     w_c = 0
#     s_c = 1
#
#     q = deque((0, 0))
#     visited[0] = True
#
#     while q:
#         node, depth = q.popleft()
#
#         for adj_node in adj_list[node]:
#             if info[adj_node] == 0:
#                 if not visited[node]:
#                     if w_c + depth >= s_c:
#                         break
#                     else:
#                         w_c += depth
#
#                 visited[node] = True
#                 q.appendleft((adj_node, 0))
#                 s_c += 1
#             else:
#                 q.append((adj_node, depth + 1))
#
#
#
#     return answer
##
# 두번째 풀이(강의 풀이)
# 브루트 포스적인(백트래킹) 풀이로 해결
# 시간복잡도: O(?)
# from collections import deque
#
# def solution(info, edges):
#     N = len(info)
#     adj_list = [[] for _ in range(N)]
#     for a, b in edges:
#         adj_list[a].append(b)
#         adj_list[b].append(a)
#
#     ans = 0
#     q = deque()
#     q.append(({0}, 1, 0))
#
#     while q:
#         cur_set, cur_sheep, cur_wolf = q.popleft()
#         ans = max(ans, cur_sheep)
#
#         next_nodes = set()
#         for node in cur_set:
#             for adj_node in adj_list[node]:
#                 if adj_node not in cur_set:
#                     next_nodes.add(adj_node)
#
#         for node in next_nodes:
#             if info[node] == 0:
#                 q.append((cur_set | {node}, cur_sheep + 1, cur_wolf))
#             elif info[node] == 1 and cur_sheep > cur_wolf + 1:
#                 q.append((cur_set | {node}, cur_sheep, cur_wolf + 1))
#
#     return ans



# 세번째 풀이(강의풀이)
# 상태 공간의 중복 처리를 처리하면 해결 가능
# 시간복잡도: O(2^17)
from collections import deque
def solution(info, edges):
    N = len(info)

    adj_list = [[] for _ in range(N)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)

    visited = set()

    ans = 0
    q = deque()
    q.append(({0}, 1, 0))

    while q:
        cur_set, cur_sheep, cur_wolf = q.popleft()
        ans = max(ans, cur_sheep)

        nxt_nodes = set()
        for node in cur_set:
            for adj_node in adj_list[node]:
                if adj_node not in cur_set:
                    nxt_nodes.add(adj_node)

        for node in nxt_nodes:
            nxt_set = cur_set | {node}
            if info[node] == 0:
                if tuple(sorted(nxt_set)) not in visited:
                    q.append((nxt_set, cur_sheep + 1, cur_wolf))
                    visited.add(tuple(sorted(nxt_set)))
            elif info[node] == 1 and cur_sheep > cur_wolf + 1:
                if tuple(sorted(nxt_set)) not in visited:
                    q.append((nxt_set, cur_sheep, cur_wolf + 1))
                    visited.add(tuple(sorted(nxt_set)))

    return ans

## 4번째 풀이(강의 풀이에서 set을 변형해서 비트마스크로 푼 풀이)
from collections import deque

def solution(info, edges):
    N = len(info)
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    q = deque()
    q.append((1 << 0, 1, 0))   # mask, sheep, wolf

    visited = set()
    visited.add(1 << 0)

    ans = 0

    while q:
        mask, sheep, wolf = q.popleft()
        ans = max(ans, sheep)

        nxt_nodes = set()

        for node in range(N):
            if mask & (1 << node):   # 현재 방문된 노드라면
                for nxt in adj[node]:
                    if not (mask & (1 << nxt)):   # 아직 방문 안 한 노드
                        nxt_nodes.add(nxt)

        for nxt in nxt_nodes:
            nxt_mask = mask | (1 << nxt)

            if info[nxt] == 0:
                if nxt_mask not in visited:
                    visited.add(nxt_mask)
                    q.append((nxt_mask, sheep + 1, wolf))
            else:
                if sheep > wolf + 1 and nxt_mask not in visited:
                    visited.add(nxt_mask)
                    q.append((nxt_mask, sheep, wolf + 1))

    return ans