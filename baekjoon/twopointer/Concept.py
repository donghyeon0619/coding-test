"""
    투포인터 알고리즘(Two-Pointer algorithm)

- 정의: 두개의 포인터(지점)을 이용하여 문제를 푸는 알고리즘
- 특징
    - 두개의 포인터를 이용할 수 있는 구조여야 한다.
    - 1차원 배열이 나오고 답의 후보를 효율적으로 탐색해야할 떄 많이 사용됨(ex 브루트푸스적 풀이일때)
"""
# BOJ 2003문제를 통한 실습

# ----------------------------------------------------
# 시작 지점과 끝 점의 모든 조합을 살펴보는 풀이 - O(N^3)
# 시자지점과 끝점을 고르는 경우가 nC2 만큼 존재
# 최악의 경우 O(N)정도가 걸리므로 시간초과가 발생함
# "않좋은" 풀이 방법
# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve
ans = 0
for left in range(N):
    for right in range(left, N):
        cur_sum = 0
        for num in arr[left:right + 1]:
            cur_sum += num
        if cur_sum == M:
            ans += 1

print(ans)

# -----------------------------------------------------
# 시작 지점과 끝점의 모든 조합을 효율적으로 살펴보는 풀이
# 방법1. 시작지점을 고정하고 모든 끝점의 후보를 살펴보기 - O(N^2)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve
ans = 0
for left in range(N):
    cur_sum = 0
    for right in range(left, N):
        cur_sum += arr[right]
        if cur_sum == M:
            ans += 1

print(ans)

# 방법 2
# 누적합 알고리즘을 이용하기 - O(N^2)
# input
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# solve
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

ans = 0
for left in range(1, N + 1):
    for right in range(left, N + 1):
        cur_sum = psum[right] - psum[left - 1]
        if cur_sum == M:
            ans += 1

print(ans)

# ----------------------------------------------------
# ----------------------------------------------------
# 위에 풀이 즉, "시작 지점과 끝 점의 모든 조합을 살펴보는 풀이는"는 효율적인 풀이로 해도
# 시간 복잡도가 O(N^2)인데 만약 범위가 높게 잡힌다면 시간초과가 발생할 확률이 있음
# 그러므로 "시작지점에 대해 합이 M이 되는 끝점은 없거나 유일하다"는 풀이로 접근해야함
# 이때 투포인터를 이용해서 사용하는데, 이분탐색을 또 이용해도 됨
# 그리고 만약 범위가 주어졌을때, 그것들을 브루트 포스적으로 하거나 효율적 풀이를 한다해도 만약
# 시간복잡도가 O(N^2)이상이 될 거 같다 하면 N을 한번 순회하고나서 O(1)나 O(logN)가 걸리는 풀이를 적용하도록 해야함
# 예를 들면 "누적합", "정렬", "DP" 등등
# 방법 1
# (누적합 알고리즘과) 이분 탐색 알고리즘을 이용해서 탐색- O(N*logN)


def is_exist(left):
    global N, M, psum

    cur = left - 1
    step = N

    while step != 0:
        while (cur + step <= N) and (psum[cur + step] - psum[left - 1] <= M):
            cur += step
        step //= 2

    return psum[cur] - psum[left - 1] == M


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# solve
psum = [0] * (N + 1)
for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

ans = 0
for left in range(1, N + 1):
    ans += is_exist(left)

print(ans)

# ------------------------------------------------------
# 방법 2
# 투 포인터 알고리즘을 이용해서 합이 M이 되는 지점을 효율적으로 탐색 - O(N)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve (two pointer)
ans = 0

right = -1
cur_sum = 0
for left in range(N):
    while (right + 1 < N) and (cur_sum + arr[right + 1] <= M):
        right += 1
        cur_sum += arr[right]

    if cur_sum == M:
        ans += 1

    cur_sum -= arr[left]

print(ans)
















