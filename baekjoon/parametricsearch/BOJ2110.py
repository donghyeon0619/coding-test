"""
문제: 공유기 설치
수준: 골드 5
"""
# 첫번째 풀이
# 못풀었슴(담에 꼭 풀어보자)
# 먼가 접근은 잘한것 같은데
# 구현을 못하겠음
# import sys
# input = sys.stdin.readline
#
# def is_possible(d):
#     global N, C, homes
#
#     m = int(1e9)
#     for h in homes:
#
#
#
#
#
# N, C = map(int, input().split())
# homes = [int(input()) for i in range(N)]
#
# max_len = homes[-1] - homes[0]
#
# cur = - 1
# step = max_len
# while step != 0:
#     while cur + step < max_len and is_possible(cur + step):
#         cur += step
#
#     step //= 2
#

# 두번쨰 풀이(강의풀이)
# 거리가 "K가"가 아닌 "K이상"이 되도록 배치 가능한가? 로 풀어야 함
# 내가 고정적거리를 생각을 했는데, 바꿔서 말아서 최소이상인가 라는 동적인 거리를 조건으로
# 접근해야지 풀 수 있음
# 최소에 최대이므로 파라매트릭 서치 알고리즘 사용
import sys
input = sys.stdin.readline

def is_possible(k):
    global N, C, homes

    bf_idx = 0
    cnt = 1
    for i in range(1, N):
        if homes[i] - homes[bf_idx] >= k:
            cnt += 1
            bf_idx = i

    return cnt >= C


N, C = map(int, input().split())
homes = sorted([int(input()) for _ in range(N)])

cur = -1
max_len = homes[-1] - homes[0] + 1

step = max_len
while step != 0:
    while cur + step < max_len and is_possible(cur + step):
        cur += step

    step //= 2


print(cur)

# 참고
# DP로도 풀 수 있는데, 시간초과 발생함
