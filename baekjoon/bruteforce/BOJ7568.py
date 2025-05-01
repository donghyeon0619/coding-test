# 덩치 문제
# 실버 5
# 풀이1
# 리뷰
# 문제에서 이미 조건들을 다 주어지므로 문제를 잘 파악하는 것이 중요, 그리고 입력 받기와 로직을 분리하는 것이 좋은 방법
# 문제가 복잡해지면 해당 역할을 구분하는 것이 테스트에 유용함
# 그리고 파이썬에서 쓸 수 있는 언패킹도 많이 활용하는 것이 좋은 듯,


import sys

readline = sys.stdin.readline
N = int(readline())
human = []
ranking = []

for i in range(N):
    cmd = list(map(int, readline().strip().split()))
    rank = 1
    human.append(cmd)
    for j in range(len(human)-1):
        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            rank += 1
        elif human[i][0] > human[j][0] and human[i][1] > human[j][1]:
            ranking[j] += 1

    ranking.append(rank)

print(*ranking)


# 풀이 2
# 내풀이랑 다르게 이 풀이는 모든 input을 받고 나서 해당 인덱스마다 나보다 덩치가 큰 값들이 몇개 있는데 비교하면서 그때마다
# output을 내는 방식임. 문제에 취지에는 이게 좀더 적절한 방법이 될 것 같기도 함


import sys
input = sys.stdin.readline
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
arr = []

for i in info:
    cnt = 0
    for j in info:
        if j[0] > i[0] and j[1] > i[1]:
            cnt += 1
    print(cnt + 1, end = ' ')

# 풀이 3
# 이 풀이도 input을 모두 받지만, 처음에 랭킹관련된 상태변수를 1로 초기화하고 for을 돌리면서 비교하는 형식으로 진행
# 그리고 언패킹 개념이 추가적으로 많이 들어가 있음
import sys

input = sys.stdin.readline

n = int(input())
a = []
res = [1] * n

for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

for i in range(n):
    x1, y1 = a[i]

    for j in range(i + 1, n):
        x2, y2 = a[j]

        if x1 < x2 and y1 < y2:
            res[i] += 1
        elif x1 > x2 and y1 > y2:
            res[j] += 1

print(*res)





