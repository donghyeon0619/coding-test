# 랜선 자르기
# 알고리즘 분류: 이분 탐색, 매개변수 탐색
# 첫번째 풀이 (틀린 풀이)
# 변수 지정도 잘못됬고, for문의 reverse를 적용했을 때 범위가 잘못됬음, 또 나눌때 0이 들어가진 않을지 주의도 해야함
# 주어진 조건에서 랜선길이가 최대 2^31-1이므로 만약 브루트 포스로 탐색을 진행하면 시간내에 끝내지 못함.
# 조건에서 범위 값이 크게 나오면 메모리 초과 및 시간초과 계속 인지
import sys

readline = sys.stdin.readline

K, N = map(int, readline().split())


lanseons = [int(readline()) for _ in range(K)]
min_val = min(lanseons)

lanseons.sort(reverse=True)

sum_val = sum(lanseons)
max_val = sum_val // N

if min_val < max_val:
    max_val = min_val


for i in range(max_val, 0, -1):
    x = N
    for j in range(len(lanseons)):
        # ZeroDivisionError 발생 주의
        x -= lanseons[j] // i

    if x <= 0:
        print(i)
        break



## 두번째 풀이
## 이분탐색을 이용한 풀이
## 이 문제는 매개 변수 탐색 유형으로, 매개 변수 탐색은 어떤 조건을 만족하는 위치 중에서 최대값이나 최솟값을 찾을 때 사용해야함
## 이 문제에서는 매개변수가 "랜선의 길이" 이고 최솟값과 최댓값은 1과 max(lan)임, 이진 탐색을 이용하여 조건을 만족하는 최대값을 구해야하

import sys
readline = sys.stdin.readline

K, N = map(int, readline().split())
lan_lengths = [int(readline()) for _ in range(K)]

lo, hi = 1, max(lan_lengths)
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    count = sum(l // mid for l in lan_lengths)

    if count >= N:
        result = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(result)

## 세번쨰 풀이
## 똑같이 이분탐색 풀이지만 여기는 end값만 허용 위에랑 비슷한 로직
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = sum(check // mid for check in lan)

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
