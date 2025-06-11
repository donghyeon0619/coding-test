# Sport Climbing Combined 문제
# 실버 5
# 첫번째 풀이
# key에서 람다를 이용한 풀이
import sys

input = sys.stdin.readline

n = int(input())

players = [tuple(map(int, input().split())) for _ in range(n)]

players.sort(key=lambda x: ((x[1] * x[2] * x[3]), (x[1] + x[2] + x[3]), x[0]))

print(players[0][0], players[1][0], players[2][0])
## 같은 풀이
# for b, p, q, r in players[:3]:
#     print(b, end=" ")
