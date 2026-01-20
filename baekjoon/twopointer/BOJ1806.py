# 부분합
# 첫번째 풀이 (내 풀이)
# 투포인터 방식으로 내가 생각한 방식으로 작성을 해봤는데
# 여기서 기존에 정했던 투포인터 방식에서 이상이므로 수정을 하는 부분이 필요

N, S = map(int, input().split())

num = list(map(int, input().split()))

ans = int(1e10)

right = -1
cur_sum = 0
for left in range(N):
    while (right + 1 < N) and (cur_sum < S):
        right += 1
        cur_sum += num[right]

    s = right - left + 1

    if cur_sum >= S and s < ans:
        ans = s

    cur_sum -= num[left]

if ans == int(1e10):
    print(0)
else:
    print(ans)


## 두번째 풀이 (강의 풀이)
## 이분탐색 이용한 풀이
## 시간복잡도: O(N*logN)
## 출발점이 고정되고, 내가 원하는 값을 찾아야할떄, 예를들면 계속 FALSE가
## 나오다가 True가 나오는 시점에 인덱스가 필요할 때 사용할 수 있음
def get_best_idx(left):
    global N, S, psum

    cur = left - 1
    step = N

    while step != 0:
        while (cur + step <= N) and (psum[cur + step] - psum[left - 1] < S):
            cur += step
        step //= 2

    return cur + 1

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# solve
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i]

ans = int(1e12)
for left in range(1, N + 1):
    right = get_best_idx(left)
    if right <= N:
        ans = min(ans, right - left + 1)

print(ans if ans != int(1e12) else 0)

## 세번쨰 풀이
## 투 포인터 알고리즘을 이용한 풀이
## 시간 복잡도: O(N)
## 내가 푼 풀이랑 비슷한 맥락이지만 여기서는 조건문을 여러번 적용해서
## 필터를 직접 구현
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# solve
ans = int(1e12)

cur_sum = 0
right = -1
for left in range(N):
    while (right + 1 < N) and (cur_sum + arr[right + 1] < S):
        right += 1
        cur_sum += arr[right]

    if cur_sum < S and right + 1 < N:
        right += 1
        cur_sum += arr[right]

    if right < N and cur_sum >= S:
        ans = min(ans, right - left + 1)

    cur_sum -= arr[left]

print(ans if ans != int(1e12) else 0)