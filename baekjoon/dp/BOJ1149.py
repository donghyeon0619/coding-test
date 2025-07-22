# RGB 거리
# 첫번쨰 풀이(틀린 풀이)
# 순차적으로 최솟값과 전에 값과 같지 않도록 했지만, 그렇게 되면 계속 최솟값을 못가져오게 될 수 있음
# 이 풀이는 그리디로 푼 것인데 이렇게 풀었을 떄 최적의 답이 안나올 수 있으므로 예외 케이스 생각하기
# 그리고 결정적으로 같은 값에 대해서 우선순위를 구하기 애매함
# 예를 들면 N번째 행에 갈 수 있는 값중 최소값이 만약 같다면 어디쪽으로 가야할지 애매해짐
# 즉: 현재 가장 낮은 값을 고르는 것 != 문제의 최적해
N = int(input())

homes = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

color = [0] * (N+1)
dp = [0] * (N+1)

m = 1001
for i in range(3):
    if homes[1][i] < m:
        m = homes[1][i]
        color[1] = i

dp[1] = m

for i in range(2, N+1):
    m = 1001
    for j in range(3):
        if homes[i][j] < m and j != color[i-1]:
            m = homes[i][j]
            color[i] = j

    dp[i] = dp[i-1] + m

print(dp[N])

# 두번쨰 풀이
# dp를 이용한 풀이 해당 행에 집에 적용되는 색깔까지에 최소비용을 구하고 각각 색깔까지에 최소 비용 도출
N = int(input())

homes = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(3):
    dp[1][i] = homes[1][i]

for i in range(2, N+1):
    for j in range(3):
        min_cost = min(
            dp[i-1][k]
            for k in range(3)
            if k != j
        )
        dp[i][j] = homes[i][j] + min_cost

print(min(dp[N]))

# 세번쨰 풀이
# 이것도 똑같이 DP를 이용한 것이지만 모든 색상에 대한 dp를 일일히 구하는 방식
# 어차피 여기서 N의 범위가 크지 않으므로 시간복잡도 면에서 많이 소요되지 않음 그러므로 일일히 해도 좋은 방식
import sys

input = sys.stdin.readline

N = int(input())
dp = []

for i in range(N):
    dp.append(list(map(int, input().split())))
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[N-1]))

# 네번째 풀이
# 세번째 풀이랑 비슷하지만 이풀이는 초기값을 처리하지 않고 푼 풀이
# 아직까지 DP를 푸는게 익숙하지 않으므로 초기값을 처리하고 푸는 것이 좋음
INF = int(1e15)

N = int(input())
costs = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N + 1)]

# DP table 갱신
for i in range(N+1):
    for j in range(3):
        best = INF
        for k in range(3):
            if k != j:
                best = min(best, dp[i-1][k])

        dp[i][j] = costs[i][j] + best

print(min(dp[N]))




