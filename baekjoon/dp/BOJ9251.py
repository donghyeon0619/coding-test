# LCS
# 골드 4
# 어떻게 풀어야할지는 알 것 같은데 이렇게 푸는 것이 맞을지 애매한 것 같음
# 못풀었다(다시 풀어봐야할듯)!!
# x = list(input())
# y = list(input())
#
# len_x = len(x)
# len_y = len(y)
#
# min_lst = 0
#
# if len_x > len_y:
#     min_lst = 1
#
# dp = []
# if min_lst == 0:
#     dp = [[0, 0] for _ in range(len_x)]
#     for i in range(len_x):
#         length = dp[i][0]
#         lst_idx = dp[i][1]
#         for j in range(dp[i][1], len_y):
#             if x[i] == y[j]:
#                 length += 1
#                 lst_idx = j
#                 break
#         dp[i][0] = length
#         dp[i][1] = lst_idx
#
#     print(max(dp, key=lambda a: a[0])[0])
#
# else:
#     dp = [[0, 0] for _ in range(len_y)]
#     for i in range(len_y):
#         length = dp[i][0]
#         lst_idx = dp[i][1]
#         for j in range(dp[i][1], len_x):
#             if y[i] == x[j]:
#                 length += 1
#                 lst_idx = j
#                 break
#         dp[i][0] = length
#         dp[i][1] = lst_idx
#
#     print(max(dp, key=lambda a: a[0])[0])

## 두번쨰 풀이
## 접근한 관계식을 수정해야함.
## 이 문제에 핵심은 dp 테이블의 각 칸에 그 위치까지의 최장 공통 부분수열의 길이를 저장해야함
## 추가적으로 그리디한 걸로 풀어도 되는지 확인할 필요x dp 풀이가 가능한지 먼저 살펴봐도 됨
# x = input().rstrip()
# y = input().rstrip()
#
# n, m = len(x), len(y)
#
# # dp[i][j] : = x[:i]와 y[:j]의 lcs 길이
# dp = [[0]*(m+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if x[i-1] == y[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[n][m])
#
#
# ## 세번쨰 풀이
# ## dp 테이블을 이차원 배열이 아닌 일차원 배열로 저장하는것
# ## 두번째 풀이와 접근방식은 동일함
# x = input().rstrip()
# y = input().rstrip()
# n, m = len(x), len(y)
#
# prev = [0]*(m+1)
# for i in range(1, n+1):
#     curr = [0]*(m+1)
#     for j in range(1, m+1):
#         if x[i-1] == y[j-1]:
#             curr[j] = prev[j-1] + 1
#         else:
#             curr[j] = max(prev[j], curr[j-1])
#     prev = curr
#
# print(prev[m])

## 네번쨰 풀이 (강의 풀이)
## 주어진 문자열 두개를 dp랑 맞추기 위해서 빈문자열 삽입
## Bottom-up 방식의 구현
# s1 = input()
# s2 = input()
#
# N, M = len(s1), len(s2)
# s1 = " " + s1
# s2 = " " + s2
#
# # 초기값 처리
# dp = [[0]*(M+1) for _ in range(N+1)]
#
# # DP table 갱신
# for n in range(1, N + 1):
#     for m in range(1, M + 1):
#         if s1[n] == s2[m]:
#             dp[n][m] = dp[n-1][m-1] + 1
#         else:
#             dp[n][m] = max(dp[n-1][m], dp[n][m-1])
#
# print(dp[N][M])

## 다섯번째 풀이(강의 풀이)
## 재귀를 이용한 Top-Down 방식의 구현
import sys
sys.setrecursionlimit(int(1e6))


def func(n, m):
    global s1, s2, dp

    # base case
    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    # recursive case
    if s1[n] == s2[m]:
        dp[n][m] = func(n-1, m-1) + 1
    else:
        dp[n][m] = max(func(n-1, m), func(n, m-1))

    return dp[n][m]


s1 = input()
s2 = input()

N, M = len(s1), len(s2),
s1 = " " + s1
s2 = " " + s2

dp = [[-1] * (M+1) for _ in range(N+1)]

print(func(N, M))
