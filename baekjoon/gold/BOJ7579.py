"""
문제: 앱
난이도: 골드3

"""
# 첫번째 풀이 (못품..)
# m을 기준으로 dp 구조를 만들시에는 메모리 초과 문제가 발생함
# 범위에서 그나마 적응 리소스를 잡아먹는 c를 기준으로 잡는것이 가장 적절함
# 아 먼가 로직은 떠올리는데 구현을 못하겠다...
# 매일 문제를 풀면서 구현력을 어떻게든 올릴러고 해야겠따.
# INF = int(1e12)
# N, M = map(int, input().split())
#
# m = [0] + list(map(int, input().split()))
# c = [0] + list(map(int, input().split()))
#
# sum_c = sum(c)
#
# dp = [[0 for _ in range(sum_c + 1)] for _ in range(N + 1)]
#
# for n in range(1, N + 1):
#     for k in range(1, sum_c + 1):
#         if k - c[n] >= 0:
#             dp[n][k] = m[n]
#         dp[n][k] = dp[n-1][k-c[n]]
# print(dp[N][M])

# 두번째 풀이 (강의 풀이)(bottom-up 방식) (top-down 방식도 가능)
# 발상의 전환을 하자
# 나는 "n번 물건까지 살펴보고, m바이트를 얻기 위한 최소비용을" 생각했지만
# 역으로 생각해서 "n번 물건까지 살펴보고, 비용 c로 얻을 수 있는 최대 메모리(바이트)"
# 로 생각하면 최소비용을 이때 구할 수가 있음
# dp는 진짜 dp table 설계가 핵심이라는 것을 알 수 있음
INF = int(1e12)
MAX = 10001

# input
N, M = map(int, input().split())

mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[0] * MAX for _ in range(N + 1)]

for n in range(1, N + 1):
    # 비용이 0일 수도 있으므로 0부터 시작해야함
    for c in range(0, MAX):
        dp[n][c] = dp[n - 1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n - 1][c - costs[n]] + mems[n], dp[n][c])

ans = INF
for c in range(0, MAX):
    if dp[N][c] >= M:
        ans = min(ans, c)

print(ans)

# 세번째 풀이
# 강의 풀이에서 좀더 최적화 함
INF = int(1e12)

# input
N, M = map(int, input().split())

mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

MAX = sum(costs) + 1

# solve
dp = [[0] * MAX for _ in range(N + 1)]

for n in range(1, N + 1):
    # 비용이 0일 수도 있으므로 0부터 시작해야함
    for c in range(0, MAX):
        dp[n][c] = dp[n - 1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n - 1][c - costs[n]] + mems[n], dp[n][c])

for c in range(0, MAX):
    if dp[N][c] >= M:
        print(c)
        break



# 네번쨰 풀이 (강의 풀이) (top-down방식)
# 재귀적 풀이도 어느정도 푸는 방법은 알고 있어야 할듯
import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e12)
MAX = 10001

def func(n, c):
    global MAX, N, mems, costs, dp

    # base case
    if n == 0:
        return 0

    if dp[n][c] != -1:
        return dp[n][c]

    # recursive case
    dp[n][c] = func(n - 1, c)
    if c - costs[n] >= 0:
        dp[n][c] = max(dp[n][c], func(n - 1, c - costs[n]) + mems[n])

    return dp[n][c]


N, M = map(int, input().split())

mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[-1] * (MAX) for _ in range(N + 1)]

ans = INF
for c in range(0, MAX):
    if func(N, c) >= M:
        ans = min(ans, c)

print(ans)






