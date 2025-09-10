"""
문제: 나무 자르기
수준: 실버 2
설명:
- 파라매트릭 서치 알고리즘을 이용해서 풀어야하는 대표적인 문제
- 파라매트릭 서치 알고리즘이란?
    : 이분 탐새을 이용하여 답을 구하는 알고리즘이며 "최대값", "최소값"을 구하는 문제를 결정 문제로 바꾸어 푸는 알고리즘

"""
# 첫번쨰 풀이
# 파라메트릭 서치를 이용해서 풀어봤지만,
# 시간초과가 발생함
# 내생각에는 시간 복잡도가 최악일떄는 O(HnlogN)이므로 이떄 시간초과가 발생함
# 그렇다면 이 for문 돌리는 쪽도 이분탐색이나 파라매트릭 서치를 사용해야할듯
# 처음 개념을 응용하는거라 그런지 어렵다
#
# N, M = map(int, input().split())
#
# def parametric_search(arr, height):
#     cur = -1
#     step = len(arr) - 1
#
#     while step != 0:
#         while cur + step < len(arr) and arr[cur + step]  == height:
#             cur += step
#         step //= 2
#     return cur
#
#
# trees = list(map(int, input().split()))
#
# trees.sort()
#
# max_height = 0
# for h in range(trees[-1], -1, -1):
#     idx = parametric_search(trees, h)
#     sum_tree = sum(trees[idx + 1:]) - (h * (len(trees) - (idx + 1)))
#     if sum_tree >= M:
#         max_height = h
#         break
#
# print(max_height)

# 두번째 풀이(강의풀이)
# 방법 1
# 파라매트릭 서치 내부안에 함수를 또 사용(이건 당연한건데, 내가 너무 일차원적으로 생각한듯)
# 결정 문제로 변환할 수 있음
# -> 결정 문제로 변환헀을때의 형태가 연속적을 나타나기 떄문에 파라매트릭 서치 사용가능
def is_possible(k):
    global N, M, heights

    num = 0
    for h in heights:
        if h > k:
            num += (h - k)

    return num >= M


N, M = map(int, input().split())
heights = list(map(int, input().split()))

# parametric search
ans = -1
left = 0
right = int(1e9)

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)

# 세번째 풀이(강의 풀이)
# 방법 2
def is_possible(k):
    global N, M, heights

    num = 0
    for h in heights:
        if h > k:
            num += (h - k)

    return num >= M


N, M = map(int, input().split())
heights = list(map(int, input().split()))

# parametric search
cur = -1
step = int(1e9) + 1
while step != 0:
    while cur + step <= int(1e9) and is_possible(cur + step):
        cur += step
    step //= 2

print(cur)

# 네번쨰 풀이(시간복잡도가 빠른 풀이)
# 이것도 비슷한 풀이 is_possible함수를 따로 선언하지 않고, 또 중복 값이 발생할 수도 있을 때를 대비해서 Counter()함수를 써서
# 딕셔너리 형태로 관리
import sys
from collections import Counter

# 입력
n, m = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.readline().split()))

s = 1
e = int(1e9)

while s <= e:
    mid = (s + e) // 2
    tot = sum((h - mid) * i for h, i in trees.items() if h > mid)

    if tot >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)



