## 행운의 문자열 문제
## 실버 1
## 첫번째 풀이
## 브루트 포스 방식으로 먼저 문자열을 입력받고 중복된 문자가 있을 경우를 대비해서 나눌 값을 구함
## 그러고 받은 모든 문자를 가지고 순열을 만들고 여기서 연속된 문자가 있는지 확인하고 있으면 break를 통해 분기하도록 진행함
## 상한O(N*N!)
import sys
import math
from itertools import combinations, permutations

input = sys.stdin.readline

s = list(input().strip())

temp = {}
order = 1

count = 0

if len(s) == 1:
    print(1)

else:
    for i in range(len(s)):
        if s[i] in temp:
            temp[s[i]] += 1
        else:
            temp[s[i]] = 1

    for i in temp.keys():
        order *= math.factorial(temp[i])

    for cur in permutations(s):
        ok = True

        for i in range(len(cur)-1):
            if cur[i] == cur[i+1]:
                ok = False
                break

        if ok:
            count += 1

    if count > 1:
        print(count // order)
    else:
        print(count)

## 두번쨰 풀이
## 강의 풀이
## 순열을 이용한 풀이
## 나랑 비슷한 풀이이지만 여기서는
## ord()랑 chr()를 이용

## 상한O(N*N!)
from itertools import permutations
import sys

input = sys.stdin.readline


def fact(x):
    if x == 0:
        return 1
    return fact(x-1) * x


S = input()
ans = 0
for perm in permutations(S):
    ok = True
    for i in range(0, len(S) -1):
        if perm[i] == perm[i+1]:
            ok = False
            break
    ans += 1

# 가독성을 위해서 ord를 사용
for i in range(ord('a'), ord('z') + 1):
    ans //= fact(S.count(chr(i)))

print(ans)

## 세번째 풀이
## 강의풀이
## 백트래킹을 이용한 풀이
## 평균이 위에 순열을 활용하는 브루트 포스 풀이보다 빠르다
## 상한 O(N*N!)을 이용
## dfs 이용한것이랑 비슷한 맥락
def func(lev):
    global S, chars, cnt, choose, ans

    # base case
    if lev == len(S):
        ans += 1
        return

    # recursive case
    for c in chars:
        if cnt[c] == 0:
            continue

        if (not choose) and (choose[-1] != c):
            cnt[c] -= 1
            choose.append(c)
            func(lev + 1)
            cnt[c] += 1
            choose.pop()


S = input()
chars = set()
cnt = dict()

for c in S:
    chars.add(c)
    if c not in cnt:
        cnt[c] = 0
    cnt[c] += 1

choose = []
ans = 0

func(0)

print(ans)
