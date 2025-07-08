# 부분 수열의 합
# 실버 2
# 첫번째 풀이
# 처음 했을 떄 틀렸는데 "부분 수열"의 정의를 제대로 알지 못해서 틀린것
# 부분 수열이란 "원래 수열에서 어떤 원소들을 골라서 남은 순서 그대로" 만드는 것이므로
# 다시 permutaion을 만들면 안됨
# 그래서 조합(combinations)을 이용해서 풀어도 됨
import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())

lst = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    for cur in combinations(lst, i):
        sum_cur = sum(cur)
        if S == sum_cur:
            cnt += 1


print(cnt)


# 두번쨰 풀이
# 부분 수열을 구현한 첫번쨰 풀이
# 리스트를 이용

def search(lev):
    global N, S, arr, choose, ans

    # base_case
    if lev == N:
        if choose and sum(choose) == S:
            ans += 1
        return

    # 인덱스가 lev인 원소 선택 O
    choose.append(arr[lev])
    search(lev+1)
    choose.pop()

    # 인덱스가 lev인 원소 선택x
    search(lev+1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
choose = []
ans = 0

search(0)

print(ans)

# 세번째 풀이
# choose리스트를 사용하는 대신 변수를 이용
def search(lev):
    global N, S, arr, cur_sum, ans

    # base case
    if lev == N:
        if cur_sum == S:
            ans += 1
        return

    # 인덱스가 lev인 원소 선택 O
    cur_sum += arr[lev]
    search(lev + 1)
    cur_sum -= arr[lev]

    # 인덱스가 lev인 원소 선택 X
    search(lev + 1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cur_sum = 0
ans = 0

search(0)
if S == 0:
    ans += 1

print(ans)

