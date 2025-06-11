# 좌표 정렬하기 문제
# 실버 5
# 첫번째 풀이
import sys

input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

for i in range(N):
    print(lst[i][0], lst[i][1])

# 두번쨰 풀이
# 리스트에 저장하지 않고 튜플에 저장

N = int(input())

dots = [tuple(map(int, input().split())) for _ in range(N)]

dots = sorted(dots)

for x, y in dots:
    print(x, y)
