"""
Programmers - 등산코스 정하기
난이도: Lv.3 (hard)
분류: 다익스트라, 파라매트릭 서치, 그래프 탐색

Author: donghyeon
Date: 2026-05-20

[문제 요약]
    - n개의 지점으로 이루어진 산에서 "출입구 → 산봉우리 → 출입구" 등산코스를 정해야 함
    - 코스 내 휴식 없이 이동해야 하는 시간 중 가장 긴 시간(= intensity)을 최소화
    - intensity가 최소인 산봉우리 번호와 그때의 intensity 값을 반환
    - intensity가 같다면 산봉우리 번호가 작은 것을 선택

[핵심 관찰]
    1. 왕복 경로지만 양방향 그래프이므로 "편도 경로의 intensity"만 구하면 됨
       (출입구 → 산봉우리의 intensity == 산봉우리 → 출입구의 intensity)
    2. intensity = "경로상 간선 가중치의 최댓값" → 일반 다익스트라(누적합)와 다른 변형
    3. "최댓값의 최솟값"을 구하는 문제 → 파라매트릭 서치도 가능
    4. 출입구가 여러 개여도 가상 노드(0)를 추가하면 단일 시작점 다익스트라로 처리 가능

[풀이 비교]
    풀이 1 (가상 노드 다익스트라):
        - 가상 노드 0을 만들어 모든 출입구와 가중치 0으로 연결
        - 노드 0에서 한 번의 다익스트라로 모든 노드까지의 최소 intensity 계산
        - 산봉우리에 도달하면 더 이상 확장하지 않음 (산봉우리 통과 금지)

    풀이 2 (역방향 다익스트라):
        - 모든 산봉우리를 동시에 출발점으로 pq에 삽입
        - heapq의 단조성 덕분에 gate에 처음 도달하는 순간 = 최적해
        - 즉시 return 가능하여 매우 효율적

    풀이 3 (파라매트릭 서치 + DFS):
        - "intensity ≤ X로 산봉우리에 도달 가능한가?"라는 결정 문제로 변환
        - 단조성(X가 가능하면 X+1도 가능) 덕분에 이진탐색 가능
        - binary lifting 방식으로 경계값을 탐색

[시간 복잡도]
    풀이 1: O(E log V)        - 다익스트라 1회
    풀이 2: O(E log V)        - 다익스트라 1회 (조기 종료로 더 빠를 수 있음)
    풀이 3: O(log W × (V+E))  - W = 최대 가중치 (1e7)

[공간 복잡도]
    풀이 1, 2: O(V + E) - 인접 리스트 + dist 배열
    풀이 3: O(V + E) - 인접 리스트 + visited 배열

[복습 포인트]
    - "코스를 여러번 방문할 수 있다"는 조건이 사실상 "왕복 = 편도"임을 내포함
    - 다중 출발점은 가상 노드로 단일 출발점으로 변환 가능
    - "최댓값의 최솟값/최솟값의 최댓값" 패턴은 파라매트릭 서치를 의심해볼 것
    - 다익스트라는 누적합뿐 아니라 max 같은 단조 증가 연산에서도 동작함
    - PriorityQueue 대신 heapq 사용 (속도 차이 큼)
    - 주어진 특수조건들이 어떤 특수한 상황을 만들 수 있는지 항상 의심할 것
"""

# =============================================================================
# 풀이 1: 가상 노드 다익스트라 (내 풀이)
# =============================================================================
# 아이디어:
#   - 가상 노드 0을 추가하고 모든 출입구와 가중치 0인 간선으로 연결
#   - 다중 출발점 문제를 단일 출발점 문제로 변환
#   - 일반 다익스트라의 "누적합" 대신 "경로상 max값"으로 dist 갱신
#   - 산봉우리에 도달하면 더 이상 인접 노드로 확장하지 않음 (통과 방지)
#
# dist[node]의 의미:
#   "노드 0에서 해당 노드까지 가는 경로 중, 경로상 최대 간선값이 가장 작은 값"
#
# 시간 복잡도: O(E log V)
# =============================================================================
import heapq

INF = int(1e12)

def solution(n, paths, gates, summits):
    answer = [INF, INF]

    set_summits = set(summits)

    # 인접 리스트 구성

    adj_list = [[] for _ in range(n + 1)]

    for i, j, n in paths:
        adj_list[i].append([j, n])
        adj_list[j].append([i, n])

    # 가상 노드 0과 모든 출입구를 가중치 0으로 연결
    for gate in gates:
        adj_list[0].append([gate, 0])

    # 다익스트라로 모든 노드까지의 최소 intensity 계산
    dist = [INF for _ in range(n + 1)]
    dist = dijkstra(0, adj_list, dist, set_summits)

    # 산봉우리 중 intensity 최소인 것 선택 (동률이면 번호가 작은 것)
    for summit in set_summits:
        if answer[1] > dist[summit]:
            answer = [summit, dist[summit]]
        elif answer[1] == dist[summit] and answer[0] > summit:
            answer[0] = summit

    return answer


def dijkstra(s, adj_list, dist, set_summits):

    pq = []
    heapq.heappush(pq, [0, s])
    dist[0] = 0

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        # 이미 더 좋은 경로로 처리된 노드는 스킵
        if cur_dist > dist[cur_node]:
            continue

        # 산봉우리는 통과 불가 (더 이상 확장하지 않음)
        if cur_node in set_summits:
            continue

        for adj_node, adj_dist in adj_list[cur_node]:
            # 핵심: 누적합이 아닌 경로상 max값으로 갱신
            max_val = max(dist[cur_node], adj_dist)
            if max_val < dist[adj_node]:
                heapq.heappush(pq, [max_val, adj_node])
                dist[adj_node] = max_val

    return dist


# =============================================================================
# 풀이 2: 역방향 다익스트라 (강의 풀이)
# =============================================================================
# 아이디어:
#   - 모든 산봉우리를 동시에 출발점으로 pq에 삽입
#   - heapq는 intensity가 작은 순으로 꺼내므로,
#     gate에 처음 도달하는 순간이 곧 전체 최적해 (조기 종료 가능)
#   - best_value를 (intensity, summit) 튜플로 두어 동일 intensity일 때
#     산봉우리 번호가 작은 것이 우선되도록 자연스럽게 처리
#
# 왜 조기 종료가 가능한가?
#   - heapq에서 꺼낸 (intensity=k, ..., gate) 시점에:
#     · 아직 큐에 남은 모든 항목은 intensity >= k
#     · max 연산은 단조 증가이므로 앞으로 더해질 경로의 intensity >= k
#   - 따라서 k보다 작은 intensity로 gate에 도달할 방법이 없음이 보장됨
#
# 시간 복잡도: O(E log V) — 조기 종료로 풀이 1보다 빠를 수 있음
# =============================================================================
import heapq

INF = int(1e12)
def solution(n, paths, gates, summits):
    gates = set(gates)

    # 그래프 만들기
    adj_list = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adj_list[i].append([j, w])
        adj_list[j].append([i, w])

    best_value = [(INF, INF) for _ in range(n + 1)]

    # solve (다익스트라)
    pq = []
    for summit in summits:
        heapq.heappush(pq, (0, summit, summit))     # (intensity, summit, cur_node)
        best_value[summit] = (0, summit)

    while pq:
        cur_intensity, init_summit, cur_node = heapq.heappop(pq)
        # gate에 도달한 첫 순간 = 전체 최적해 (조기 종료)

        if cur_node in gates:
            return (init_summit, cur_intensity)

        for adj_node, adj_time in adj_list[cur_node]:
            nxt_intensity = max(cur_intensity, adj_time)
            # 튜플 비교로 (intensity 우선, 동률 시 산봉우리 번호) 자연 처리
            if (nxt_intensity, init_summit) < best_value[adj_node]:
                heapq.heappush(pq, (nxt_intensity, init_summit, adj_node))
                best_value[adj_node] = (nxt_intensity, init_summit)



# =============================================================================
# 풀이 3: 파라매트릭 서치 + DFS (강의 풀이)
# =============================================================================
# 아이디어:
#   - "intensity가 X 이하인 등산코스가 존재하는가?"라는 결정 문제로 변환
#   - 단조성: X로 도달 가능 ⇒ X' > X로도 도달 가능
#   - 따라서 "도달 불가능한 최대 X"를 찾고 +1 하면 답
#
# 탐색 알고리즘 (binary lifting 스타일):
#   - step을 1e7부터 시작해 절반씩 줄여가며 cur을 최대한 키움
#   - solve(cur + step)이 비어있는 동안(= 도달 불가) cur += step
#   - 못 늘리면 step //= 2로 더 정밀하게 접근
#   - 최종 cur = 도달 불가능한 최대 threshold → 답은 cur + 1
#
# 단조성 시각화:
#   threshold:  1  2  3  ...  cur cur+1  ...  1e7
#   도달가능:   F  F  F  ...   F    T    ...   T
#                              ↑    ↑
#                            마지막F 첫T(=답)
#
# 시간 복잡도: O(log W × (V + E))   W = 최대 가중치 (1e7)
# =============================================================================
import sys
sys.setrecursionlimit(int(1e6))

def dfs(node, threshold):
    global n, paths, gates, summits, adj_list, visited, types, candidates

    # base case
    if visited[node]: return
    visited[node] = True

    if types[node] == 'summit':
        candidates.append(node)
        return

    # recursive case
    for nxt, w in adj_list[node]:
        if w <= threshold:
            dfs(nxt, threshold)

def solve(threshold):
    global n, paths, gates, summits, adj_list, visited, types, candidates

    candidates = []
    visited = [False] * (n + 1)
    for gate in gates:
        if not visited[gate]:
            dfs(gate, threshold)

    return candidates

def solution(_n, _paths, _gates, _summits):
    global n, paths, gates, summits, adj_list, visited, types, candidates
    n, paths, gates, summits = _n, _paths, _gates, _summits

    types = ['X'] * (n + 1)
    for gate in gates:
        types[gate] = 'gate'
    for summit in summits:
        types[summit] = 'summit'

    # 그래프 만들기
    adj_list = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        adj_list[i].append([j, w])
        adj_list[j].append([i, w])

    # 파라매트릭 서치 (binary lifting 방식)
    # cur = "도달 불가능한 최대 threshold"를 찾음
    cur = 0
    step = int(1e7)
    while step != 0:
        while cur + step <= int(1e7) and len(solve(cur + step)) == 0:
            cur += step
        step //= 2

    # cur + 1 = 도달 가능한 최소 threshold = 정답 intensity
    candidates = solve(cur + 1)
    return min(candidates), cur + 1
