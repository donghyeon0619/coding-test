# SWEA D2
# 최빈수 구하기
# 첫번째 풀이
# for문과 조건식을 이용한 정석풀이(코딩 테스트에서는 이렇게만 풀어도 괜찮음)
T = int(input())

for i in range(1, T+1):
    t = int(input())
    nums = dict()
    temp = [x for x in map(int, input().split())]

    for j in temp:
        if j not in nums:
            nums[j] = 1
        else:
            nums[j] += 1

    max_freq = max(nums.values())
    freq_value = max(num for num, freq in nums.items() if freq == max_freq)

    print(f"#{t} {freq_value}")

## 두번째 풀이
## Counter 라이브러리를 이용한 풀이
from collections import Counter

T = int(input())

for i in range(1, T+1):
    t = int(input())
    nums = [x for x in map(int, input().split())]

    cnt = Counter(nums)

    max_cnt = max(cnt.values())
    ans = max(num for num, c in cnt.items() if c == max_cnt)
    print(f"#{t} {ans}")
