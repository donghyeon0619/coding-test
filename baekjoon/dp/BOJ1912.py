"""
문제: 연속합
난이도: 실버2
"""
# 첫번째 풀이
# 이중 for문에다가 sum함수도 사용해서 시간복잡도가 N^3이 나옴 범위가 10만이라 시간초과 발생
# N = int(input())
# arr = list(map(int, input().split()))
#
# dp = [-1001 for _ in range(N+1)]
#
# for i in range(1, N + 1):
#     best = 0
#     for j in range(0, i):
#         best = max(best, sum(arr[j:i - 1]))
#
#     dp[i] = max(dp[i - 1], best + arr[i - 1])
#
# print(max(dp))
#
# # 두번째 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 초기값 설정
end_here = arr[0]  # arr[0]로 끝나는 최대합
best = arr[0]  # 전체 중 최대합

# 1부터 n-1까지 순회
for i in range(1, n):
    # i를 포함해서 끝내는 최대합
    end_here = max(end_here + arr[i], arr[i])
    # 전체 최대합 갱신
    best = max(best, end_here)

print(best)

#
# # 세번째 풀이
# # Kadane's algorithm
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# dp[i]: arr[0..i] 구간 중 반드시 i에서 끝나는 최대 연속합
dp = [0] * N
dp[0] = arr[0]
ans = dp[0]

for i in range(1, N):
    # i까지의 구간을 연장할지, 새로 시작할지 결정
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    ans = max(ans, dp[i])

print(ans)

# 네번째 풀이(강의 풀이)
# dp[n] : n번 원소에서 끝나게 연속된 원소를 선택했을 때 합의 최대값
# bottom-up 풀이
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N + 1)]
for n in range(1, N + 1):
    dp[n] = max(dp[n - 1], 0) + arr[n]

print(max(dp[1:]))

# 다섯번째 풀이(강의 풀이)
# top-down 방식
import sys
sys.setrecursionlimit(int(1e6))
INF = int(1e12)

def func(n):
    global N, arr, dp

    # base case
    if n == 0:
        return 0
    if dp[n] != -INF:
        return dp[n]

    # recursive case
    dp[n] = max(0, func(n-1)) + arr[n]

    return dp[n]


# input
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-INF] * (N + 1)
ans = -INF
for n in range(1, N + 1):
    ans = max(ans, func(n))

print(ans)

