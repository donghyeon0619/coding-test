# 카드 문제
# 알고리즘 분류 : 자료구조, 정렬, 해시를 사용한 집합 과 맵
# 첫번째 풀이
# 어느정도 잘 짠 거 같지만, 딕셔너리의 get()함수라든가, key값을 int로 미리 선언해서
# strip()함수를 호출하는 것을 줄이도록 하면 좀더  예쁘게 짤 수 있을 듯
import sys

readline = sys.stdin.readline

N = int(readline())
x = dict()

for _ in range(N):
    num = readline()
    # 해당 key가 있는지 확인
    if num not in x:
        x[num] = 1
    else:
        x[num] += 1

max_value = max(x.values())
keys = [int(k) for k, v in x.items() if v == max_value]

if len(keys) == 1:
    print(keys[0])
else:
    keys.sort()
    print(keys[0])


## 두번째 풀이
## sort 부분에 람다를 이용
import sys

readline = sys.stdin.readline

N = int(readline())
nums = {}

for _ in range(N):
    num = int(readline())
    # 해당 key가 있는지 확인
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

# dsu 패턴으로 동작하므로 불필요한 오버헤드 발생 가능
# items()는 (key, value) 쌍의 튜플 반환
nums = sorted(nums.items(), key=lambda x: (x[1], -x[0]))

print(nums[-1][0])

## 세번째 풀이
## min, max를 잘 이용했고 get()함수를 이용한 풀이
import sys
input = sys.stdin.readline

n = int(input())
dic = {}

# 숫자의 빈도 계산
for _ in range(n):
    num = int(input())
    dic[num] = dic.get(num, 0) + 1

# 가장 큰 빈도수를 찾고, 빈도수가 같은 경우 가장 작은 숫자를 선택
max_freq = max(dic.values())
most_frequent_number = min(num for num, freq in dic.items() if freq == max_freq)

print(most_frequent_number)

# 4번쨰 풀이
# 딕셔너리 상속받은 Counter 클래스 이용
import sys
from collections import Counter

readline = sys.stdin.readline
N = int(readline())

cards = [int(readline()) for _ in range(N)]
cnt = Counter(cards)

max_cnt = max(cnt.values())
answer = min(num for num, c in cnt.items() if c == max_cnt)
print(answer)