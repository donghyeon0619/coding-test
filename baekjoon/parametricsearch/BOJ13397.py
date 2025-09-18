"""
문제: 구간 나누기2
수준: 골드 4
리뷰:
내가 생각했던 것과 전혀 달랐던 사고로 풀은 문제, 다른 시선으로 생각해볼 수 있게 된듯
다시 풀면 좋을 문제
"""
# 첫번째 풀이(못품 다시 풀어야할듯)
# 로직은 알겠는데
# 배열을 M개 이하의 구간으로 나누는 방법을 구현할줄 알아야할 것 같음
# def is_possible(k):
#     global N, M
#
#     max_value = 0
#     for m in range(1, M + 1):
#
#
#
# # 첫번쨰 풀이
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# min_num = min(arr)
# max_num = max(arr)
#
# end = max_num - min_num
#
# cur = -1
# step = end + 1
#
# while step != 0:
#     while cur + step < end + 1 and is_possible(cur + step):
#         cur += step
#     step //= 2
#
# print(cur)

# 두번째 풀이(강의 풀이)
# 시간복잡도: O(10,000 * N)
# "N개를 M개의 그룹으로 나누는 모든 경우를 살펴보는 브루트스적 풀이"는 불가능하지만
# "답의 후보에 대해 모두 살펴 보는 풀이"는 가능함
# 답의 후보에 대해 모두 살펴보는 풀이 = 구간의 점수의 최대값이 k이하가 되도록 할 수 있는가?
# 마지막에 linear search를 함
import sys
input = sys.stdin.readline

def is_possible(k): # return True if k이하가 가능하면
    global N, M, arr

    cur_mn = arr[0]
    cur_mx = arr[0]
    cnt = 0 # 현재까지 만들어진 구간의 개수 - 1

    for i in range(1, N):
        cur_mn = min(cur_mn, arr[i])
        cur_mx = max(cur_mx, arr[i])

        if cur_mx - cur_mn > k:
            cur_mn = arr[i]
            cur_mx = arr[i]
            cnt += 1
    cnt += 1

    return cnt <= M

# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, max(arr) - min(arr),

# solve (linear search)
ans = -1
for i in range(start, end + 1):
    if is_possible(i):
        ans = i
        break

print(ans)

# 세번째 풀이(강의 풀이)
# 답의 후보에 대해 파라매트릭 서치를 이용하여 살펴보는 풀이
# 시간 복잡도: O(14*N)
import sys
input = sys.stdin.readline


def is_possible(k):
    global N, M, arr

    cur_mn = arr[0]
    cur_mx = arr[0]

    # 현재까지 만들어진 구간의 개수 - 1
    cnt = 0

    for i in range(1, N):
        cur_mn = min(cur_mn, arr[i])
        cur_mx = max(cur_mx, arr[i])

        if (cur_mx - cur_mn) > k:
            cur_mn = arr[i]
            cur_mx = arr[i]
            cnt += 1
    cnt += 1

    return cnt <= M


# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))


end = max(arr) - min(arr)
# solve (parametric search)
cur = -1
step = end + 1

while step != 0:
    while cur + step <= end and not is_possible(cur + step):
        cur += step
    step //= 2

print(cur + 1)

# 네번쨰 풀이 (다른 사람 풀이)
# 여기는 파라매트릭 서치를 사용하지 않고
# 이분탐색을 사용해서 최대값에 최소값을 찾는 방법
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, max(nums) - min(nums),
ans = 0


def is_valid(mid):
    min_num = max_num = nums[0]
    cnt = 1

    for num in nums:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        if max_num - min_num > mid:
            cnt += 1
            min_num = max_num = num
            if cnt > M:
                return False

    return True


while start <= end:
    mid = (start + end) // 2

    if is_valid(mid):
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)









































