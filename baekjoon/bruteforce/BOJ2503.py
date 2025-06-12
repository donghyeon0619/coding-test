# 숫자야구
# 브루트포스 문제
# 순열과 브루트 포스를 이용해서 풀이
# 첫번째 풀이
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
infos = [input().split() for _ in range(N)]
ans = 0

for cur in permutations(range(1, 10), 3):
    ok = True

    for num, st, bl in infos:
        cur_st = cul_bl = 0

        for i in range(3):
            if str(cur[i]) == num[i]:
                cur_st += 1
            elif str(cur[i]) in num:
                cul_bl +=1

        if cur_st != int(st) or cul_bl != int(bl):
            ok = False
            break

    if ok:
        ans += 1

print(ans)

## 두번째 풀이


