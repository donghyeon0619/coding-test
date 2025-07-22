# 배낭 문제
# 골드 5
# (못 푼 문제이므로 다시 풀어봐야 함)
# 관계식은 어느정도 생각은 했지만
# 무게와 가치를 따로 둔 배열변수 선언 및 구현등에서 생각을 못해냄
# 다음에 다시 풀어서 구현력을 늘려야 할 것 같음
# 첫번째 풀이(강의 풀이)
# bottom-up 방식
# N, K = map(int, input().split())
#
# W = [0]
# V = [0]
#
# for _ in range(N):
#     w, v = map(int, input().split())
#     W.append(w)
#     V.append(v)
#
# dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
#
# for n in range(1, N + 1):
#     for k in range(1, K+1):
#         dp[n][k] = dp[n-1][k]
#         if k - W[n] >= 0:
#             dp[n][k] = max(dp[n][k], dp[n-1][k - W[n]] + V[n])
#
#
# print(dp[N][K])

# 두번째풀이
# top-down 풀이
# 이 문제에서는 부분부분만 구하면 되므로 굳이 bottom-up 처럼 전체 값을 구할 필요는 없음
# 실제로 백준에서도 bottom-up보다는 시간을 많이 단축시킴
import sys
sys.setrecursionlimit(int(1e6))

def func(n, k):
    global W, V, dp

    # base case
    if n == 0 or k == 0:
        return 0

    if dp[n][k] != -1:
        return dp[n][k]

    # recursive case
    dp[n][k] = func(n-1, k)
    if k - W[n] >= 0:
        dp[n][k] = max(dp[n][k], func(n - 1, k - W[n]) + V[n])

    return dp[n][k]


N, K = map(int, input().split())

W = [0]
V = [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[-1 for _ in range(K+1)] for _ in range(N+1)]

print(func(N, K))


