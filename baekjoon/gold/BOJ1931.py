"""
문제: 회의실 배정
수준: 골드 5
리뷰:
"""
## 첫번째 풀이 (내풀이)
## 맟췄지만 다른 사람들 푼것에 비해서
## 시간복잡도가 오래 걸렸음
## 먼저 첫번쨰 이유는 N의 범위가 10만개로 엄청 크므로
## 파이썬 내장함수인 input()을 쓰는 거보단 sys.stdin.readline()을 쓰는 것이 속도가 빠름
import sys
input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting = sorted(meeting, key=lambda x: (x[0], x[1]-x[0],))

best = 1
stack = [meeting[0]]
idx = 0

while stack:

    s, e = stack.pop()

    for i in range(idx + 1, N):
        if meeting[i][0] > s and meeting[i][1] < e:
            idx = i
            stack.append(meeting[i])
            break

        elif meeting[i][0] >= e:
            best += 1
            idx = i
            stack.append(meeting[i])
            break

print(best)

# 두번쨰 풀이(강의 풀이)
# 보통 그리디 풀이는 정렬과 많이 쓰임
# 여기서는 끝점을 기준으로 정렬을 하고 끝점이 작은점중에서 가능한 것들 추려서 풀었음
# 그리고 나는 단순히 숫자만 나열했는데,
# 여기서는 그래프를 통해서 각각의 좌표에 대해서 시각적으로 풀어서
# 좀더 풀이가 잘 보였음
import sys
input = sys.stdin.readline

# input
N = int(input())

times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))

# solve
# 여기서 마지막 파라미터에 x[0]을 준 이유는 만약 start랑, end가 같을 때,
# 그때 만약 end랑 같은 다른 값이 존재하는데 이때 start가 더 작은 값이 나중에 나오게 되도
# 오름차순으로 정렬이 안되므로 여기서 포함시켜줘야하는 듯
times = sorted(times, key=lambda x: (x[1], x[0]))

ans = 0
end = 0
for s, e in times:
    if s >= end:
        ans += 1
        end = e

print(ans)


# 세번째 풀이(강의 풀이)
# dp로 인한 풀이이지만, dp로 풀었을 때 배열의 메모리초과가 발생할 수 있으므로
# 좌표 압축이라는 개념을 도입해서 풀었음
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

nums = []
times = []

for _ in range(N):
    s, e = map(int, input().split())
    times.append((s, e))
    nums.append(s)
    nums.append(e)

# coordinate compression (좌표 압축)
nums = sorted(list(set(nums)))
T = len(nums)

convert = dict()
for idx, num in enumerate(nums, 1):
    convert[num] = idx

# solve
starts = dict()
for i in range(N):
    tmp0, tmp1 = convert[times[i][0]], convert[times[i][1]]
    if tmp1 in starts:
        starts[tmp1].append(tmp0)
    else:
        starts[tmp1] = [tmp0]

for key in starts:
    starts[key].sort()

dp = [0] * (T + 1)
for t in range(1, T + 1):
    dp[t] = dp[t - 1]
    if t in starts:
        for s in starts[t]:
            dp[t] = max(dp[t], dp[s] + 1)

print(dp[T])

