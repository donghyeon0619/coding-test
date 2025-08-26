"""
문제: 가장 긴 바이토닉 부분 수열
난이도: 골드 5
중요도: 상
리뷰: 발상의 전환이 필요한 것 같고 다른 방식으로 생각하는 생각의 스펙트럼을 넓힐 수 있는 계기였던 것 같음
그리고 이문제는 배웠던 개념을 응용하는 것 여기서는 LIS를 두번 사용한 방법
"""
# 첫번쨰 풀이 (못풀었음)
# feedback: 문법적인 문제도 있었고, 반례를 생각하지 못했던 것도 문제가 있었음
# 해당 for문을 돌렸을 때 반례가 있는지 이식해서 사용해야할듯
# 근데 종합적으로 LIS로 접근하면 안되는 것 로직 자체가 미숙한게 많앗음
# N = int(input())
# arr = [0] + list(map(int, input().split()))
# dp = [[] for _ in range(N + 1)]
#
# dp[1].append(arr[1])
# for i in range(2, N+1):
#     if dp[i - 1][-1] < arr[i]:
#         temp = [arr[i]]
#         # 이 부분은 그리디한 풀이 이므로 만약 엄청 낮은 값이 나오면 그 이후에 나오는 더 좋은
#         # 결과값들을 불러오지 못할 수도 있음
#         for j in range(i-1, 0, -1):
#             if arr[j] < temp[-1]:
#                 temp.append(arr[j])
#
#         dp[i] = max([*dp[i - 1], temp], key=len)
#
#     elif dp[i - 1][-1] == arr[i]:
#         dp[i] = dp[i-1]
#
#     else:
#         temp = dp[i-1]
#         dp[i].append(temp.append(arr[i]))
#
# print(len(dp[N]))

# 두번쨰 풀이
# dp를 두번 사용(이중 for문을 이용)
# N = int(input())
# A = list(map(int, input().split()))
#
# # inc[i]: i에서 끝나는 LIS 길이
# inc = [1] * N
# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             inc[i] = max(inc[i], inc[j] + 1)
#
# # dec[i]: i에서 시작하는 "감소" 부분 수열의 길이
# dec =[1] * N
# for i in range(N - 1, -1, -1):
#     for j in range(N - 1, i, -1):
#         if A[j] < A[i]:
#             dec[i] = max(dec[i], dec[j] + 1)
#
# ans = max(inc[i] + dec[i] - 1 for i in range(N))
# print(ans)

# 세번쨰 풀이(강의 풀이) (bottom-up 방식)
# 이 풀이도 똑같이 LIS를 두번 활용한풀이
N = int(input())
arr = [0] + list(map(int, input().split()))

# solve
dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)
dp1[1] = dp2[N] = 1

# dp1
for n in range(2, N + 1):
    dp1[n] = 1
    # dp1[n] 갱신
    for i in range(1, n):
        if arr[n] > arr[i]:
            dp1[n] = max(dp1[n], dp1[i] + 1)


# dp2
for n in range(N - 1, 0, -1):
    dp2[n] = 1
    for i in range(N, n, -1):
        if arr[n] > arr[i]:
            dp2[n] = max(dp2[n], dp2[i] + 1)

ans = 0
for n in range(1, N + 1):
    ans = max(ans, dp1[n] + dp2[n] - 1)

print(ans)

# 4번쨰 풀이 (강의 풀이)(top-down방식)
def func1(n):
    global N, arr, dp1

    # base case:
    if dp1[n] != -1:
        return dp1[n]

    # recursive case:
    dp1[n] = 1
    for i in range(1, n):
        if arr[n] > arr[i]:
            dp1[n] = max(dp1[n], func1(i) + 1)

    return dp1[n]


def func2(n):
    global N, arr, dp2

    # base case
    if dp2[n] != -1:
        return dp2[n]

    # recursive case
    dp2[n] = 1
    for i in range(N, n, -1):
        if arr[n] > arr[i]:
            dp2[n] = max(dp2[n], func2(i) + 1)

    return dp2[n]


# input
N = int(input())
arr = [0] + list(map(int, input().split()))

# solve
dp1 = [-1] * (N + 1)
dp2 = [-1] * (N + 1)

dp1[1] = dp2[N] = 1

ans = 0
for n in range(1, N + 1):
    ans = max(ans, func1(n) + func2(n) - 1)

print(ans)
