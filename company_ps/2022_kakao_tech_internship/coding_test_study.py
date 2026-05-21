"""
Programmers - 코딩테스트 공부
난이도: hard
분류:

Author: donghyeon
Date: 2026-05-11

[문제 요약]
- 코딩 테스트 문제를 풀기 위해서는 알고력(alp)과 코딩력(cop)이 필요하다.
- 각 문제는 요구 알고력, 요구 코딩력, 보상 알고력, 보상 코딩력, 풀이 비용을 가진다.
- 현재 풀 수 있는 문제는 여러 번 풀 수 있으며, 알고리즘 공부와 코딩 공부를 통해 각각의 능력치를 1씩 올릴 수도 있다.
- 목표는 모든 문제를 한 번씩 푸는 것이 아니라,
  모든 문제를 풀 수 있는 알고력과 코딩력에 도달하는 최소 시간을 구하는 것이다.

[핵심 관찰]
- 최종 목표는 모든 문제의 요구 알고력 최댓값과 요구 코딩력 최댓값에 도달하는 것이다.
- 문제를 요구 능력치 기준으로 정렬한 뒤 그때그때 최소 선택을 하는 그리디 방식은 최적해를 보장하지 않는다.
- 현재 상태에서 어떤 문제를 푸느냐에 따라 이후 도달 가능한 상태와 비용이 달라지므로,
  (알고력, 코딩력)을 하나의 상태로 보고 최소 시간을 관리해야 한다.
- dp[a][c] = 알고력 a, 코딩력 c에 도달하는 최소 시간으로 정의할 수 있다.
- 목표 능력치를 초과하는 값은 더 구분할 필요가 없으므로 target_alp, target_cop로 압축한다.

[풀이 비교]
1. 그리디 접근
   - 문제를 정렬한 뒤 현재 부족한 능력치를 가장 싸게 채우려는 방식이다.
   - 하지만 현재의 최선 선택이 전체 최단시간을 보장하지 않아 실패한다.

2. 2차원 DP
   - 공부와 문제 풀이를 각각 별도 로직으로 처리한다.
   - 현재 상태에서 알고리즘 공부, 코딩 공부, 풀 수 있는 문제 풀이를 통해 다음 상태를 갱신한다.
   - Bottom-up 방식이며, 현재 상태의 최소 시간을 다음 상태로 넘겨주는 형태이다.

3. 2차원 DP 개선
   - 알고리즘 공부와 코딩 공부를 가상의 문제로 추가한다.
   - 공부와 문제 풀이를 하나의 반복문에서 동일하게 처리할 수 있어 코드가 더 간결해진다.

4. 다익스트라
   - 알고력과 코딩력을 좌표 상태로 보고 그래프 최단거리 문제로 해석한다.
   - 상태는 (알고력, 코딩력), 간선은 공부 또는 문제 풀이, 간선 비용은 걸리는 시간이다.
   - 모든 비용이 양수이므로 다익스트라를 사용할 수 있다.

[시간 복잡도]
- DP 풀이:
  O(target_alp * target_cop * N)
  N은 problems의 길이이다.
  제한상 target_alp, target_cop는 최대 150이므로 충분히 가능하다.

- 다익스트라 풀이:
  O(target_alp * target_cop * N * log(target_alp * target_cop))
  우선순위 큐를 사용하므로 log 비용이 추가된다.

[공간 복잡도]
- O(target_alp * target_cop)
- 각 알고력/코딩력 상태에 대한 최소 시간을 저장하기 위해 2차원 배열을 사용한다.

[복습 포인트]
- 이 문제는 문제 순서가 중요한 것이 아니라, 능력치 상태별 최소 시간이 중요하다.
- 목표를 초과하는 능력치는 목표값으로 압축해도 된다.
- 공부도 "요구 능력치 0, 보상 +1, 비용 1"인 문제로 볼 수 있다.
- 상태 이동 비용이 모두 양수이므로 DP뿐 아니라 다익스트라로도 해석할 수 있다.

"""
# 첫 번째 풀이 - 그리디 접근 실패
# 문제를 요구 알고력/코딩력 기준으로 정렬한 뒤,
# 현재 풀 수 있는 문제와 공부를 비교하여 그때그때 최소 비용을 선택하려고 했다.
# 하지만 현재 시점의 최소 선택이 전체 최단시간을 보장하지 않는다.
# 또한 같은 문제를 여러 번 풀 수 있고, 문제 풀이 순서에 따라 이후 선택지가 달라지므로
# 단순 정렬 + 순차 처리 방식으로는 모든 경우를 올바르게 고려하기 어렵다.
# 따라서 이 문제는 그리디보다는 상태별 최소 비용을 저장하는 DP 접근이 적합하다.
#
# def solution(alp, cop, problems):
#     answer = 0
#     can_solve_idx = -1
#
#     problems.sort(key=lambda x: (x[0], x[1]))
#
#     for problem in problems:
#         if alp >= problem[0] and cop >= problem[1]:
#             can_solve_num += 1
#
#         if problem[0] > alp or problem[1] > cop:
#             cost = 0
#
#             if alp - problem[0] < 0:
#                 cost += problem[0] - alp
#
#             if cop - problem[1] < 0:
#                 cost += problem[1] - cop
#
#             for i in range(can_solve_idx + 1):
#                 n = 0
#                 temp_alp = alp
#                 temp_cop = cop
#                 while temp_alp >= problem[0] and temp_cop >= problem[1]:
#                     temp_alp += problems[i][2]
#                     temp_cop += problems[i][3]
#                     n += 1
#                 cost = min(cost, problem[i][4] * n)
#
#     return answer

# 두번째 풀이
# dp를 이용한 풀이
# 두 번째 풀이 - 2차원 DP
# dp[a][c] = 알고력 a, 코딩력 c에 도달하는 최소 시간으로 정의한다.
# 목표는 모든 문제를 직접 푸는 것이 아니라,
# 모든 문제를 풀 수 있는 최소 알고력/코딩력에 도달하는 것이다.
# 각 상태에서 가능한 행동은 알고리즘 공부, 코딩 공부, 현재 풀 수 있는 문제 풀이이다.
# 공부는 한 능력치를 1 올리는 이동이고, 문제 풀이는 보상만큼 능력치를 올리는 이동이다.
# 목표 능력치를 초과하는 경우에는 target_alp, target_cop로 압축하여 처리한다.
def solution(alp, cop, problems):

    INF = int(1e15)

    target_alp = max(problem[0] for problem in problems)
    target_cop = max(problem[1] for problem in problems)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    for n in range(alp, target_alp + 1):
        for k in range(cop, target_cop + 1):
            # 1. 알고리즘 공부
            next_alp = min(target_alp, n + 1)
            dp[next_alp][k] = min(dp[next_alp][k], dp[n][k] + 1)

            # 2. 코딩 공부
            next_cop = min(target_cop, k + 1)
            dp[n][next_cop] = min(dp[n][next_cop], dp[n][k] + 1)

            # 3. 문제풀이
            for problem in problems:
                if n >= problem[0] and k >= problem[1]:
                    next_alp = min(target_alp, n + problem[2])
                    next_cop = min(target_cop, k + problem[3])
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[n][k] + problem[4])

    return dp[target_alp][target_cop]

# 세 번째 풀이 - 2차원 DP, 공부를 문제처럼 처리
# 두 번째 풀이와 같은 2차원 DP 접근이다.
# 차이점은 알고리즘 공부와 코딩 공부를 별도 로직으로 작성하지 않고,
# 각각 [0, 0, 1, 0, 1], [0, 0, 0, 1, 1] 형태의 가상 문제로 추가한다는 점이다.
# 즉, 공부도 "요구 능력치 0, 보상 +1, 비용 1인 문제"로 보고
# 모든 행동을 하나의 반복문에서 동일하게 처리한다.
# dp[a][c] = 알고력 a, 코딩력 c에 도달하는 최소 시간으로 정의하며,
# 현재 상태에서 풀 수 있는 모든 문제를 확인한 뒤 다음 상태로 최소 시간을 넘겨준다.
# 목표 능력치를 초과하는 경우에는 target_alp, target_cop로 압축한다.
INF = int(1e12)

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    target_alp = max([problem[0] for problem in problems] + [alp])
    target_cop = max([problem[1] for problem in problems] + [cop])

    # dp
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    for ap in range(alp, target_alp + 1):
        for cp in range(cop, target_cop + 1):
            for aq, cq, ad, cd, cost in problems:
                if ap >= aq and cp >= cq:
                    nxt_ap = min(target_alp, ap + ad)
                    nxt_cp = min(target_cop, cp + cd)
                    dp[nxt_ap][nxt_cp] = min(dp[nxt_ap][nxt_cp], dp[ap][cp] + cost)

    return dp[target_alp][target_cop]

# 네 번째 풀이 - 다익스트라
# 알고력과 코딩력을 하나의 좌표 상태로 보고 그래프 최단거리 문제로 해석한 풀이이다.
# 상태는 (알고력, 코딩력), 간선은 공부 또는 문제 풀이, 간선 비용은 걸리는 시간이다.
# 알고리즘 공부와 코딩 공부는 세 번째 풀이처럼 가상 문제로 추가하여 동일하게 처리한다.
# 모든 행동 비용은 1 이상이므로 음수 간선이 없고, 따라서 다익스트라를 사용할 수 있다.
# 우선순위 큐에는 현재까지 걸린 시간과 현재 능력치 상태를 넣고,
# 가장 시간이 적게 걸린 상태부터 꺼내 다음 상태를 갱신한다.
# 이미 더 짧은 시간으로 방문한 상태라면 건너뛰고,
# 목표 상태가 우선순위 큐에서 꺼내지는 순간 해당 시간이 최단시간이므로 바로 반환한다.
# 목표 능력치를 초과하는 경우에는 target_alp, target_cop로 압축한다.
import heapq

INF = int(1e12)

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    target_alp = max([problem[0] for problem in problems] + [alp])
    target_cop = max([problem[1] for problem in problems] + [cop])

    time = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]

    # solve (dijkstra)
    pq = []
    heapq.heappush(pq, (0, alp, cop))
    time[alp][cop] = 0

    while pq:
        cur_time, cur_alp, cur_cop = heapq.heappop(pq)

        if cur_time > time[cur_alp][cur_cop]:
            continue
        if cur_alp >= target_alp and cur_cop >= target_cop:
            return cur_time

        for aq, cq, ad, cd, cost in problems:
            if cur_alp >= aq and cur_cop >= cq:
                nxt_time = cur_time + cost
                nxt_alp = min(target_alp, cur_alp + ad)
                nxt_cop = min(target_cop, cur_cop + cd)
                if nxt_time < time[nxt_alp][nxt_cop]:
                    time[nxt_alp][nxt_cop] = nxt_time
                    heapq.heappush(pq, (nxt_time, nxt_alp, nxt_cop))

    return time[target_alp][target_cop]