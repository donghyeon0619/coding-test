"""
문제: 개똥벌레
수준: 골드 5
"""
# 첫번째 풀이
# 이분탐색을 좀 수정해야할 것 같은데 좀 맨정신이고 집중 잘될떄 다시 해봐야겠다.
# lowee bound의 인덱스 값을 가져와야 하므로 그것에 대한 생각이 필요
# 기존 배운 이분탐색에서 응용해서 변경할줄 알아야 할듯
# 그리고 이것도 기존 개념문제 다시본거라 좀더 생각 많이하면서 풀어야 할듯
import sys
input = sys.stdin.readline

def binary_search(arr, num, l):
    cur = -1
    step = l

    while step != 0:
        while cur + step < l and arr[cur + step] < num:
            cur += step

        step //= 2

    return cur + 1


s = []
j = []
p = []

N, H = map(int, input().split())
for n in range(N):
    num = int(input())
    if n % 2 == 0:
        s.append(num)
    else:
        j.append(num)

s.sort()
j.sort()
l = N//2

for h in range(1, H + 1):
    idx1 = binary_search(s, h, l)
    idx2 = binary_search(j, H-h + 1, l)

    cnt = (l - idx1) + (l - idx2)
    p.append(cnt)

# p.sort()
# count = 1
# min_val = p[0]
#
# for i in range(1, len(p)):
#     if p[i] > min_val:
#         print(min_val, count)
#
#         break
#     else:
#         count += 1
# 위에 코드보단
min_val = min(p)
count = p.count(min_val)
print(min_val, count)

# 두번째 풀이(두번째 풀이)
# 풀이법: 장애물의 높이를 카운팅하여 처리
# 시간복잡도: O(N + H)
# 리뷰
# dp처럼 상대위치로 품
# 여기서 주목할 점이 top에 대해서 나는 내려서 생각을 했지만,
# 여기서는 높이릉 고정으로 잡아서 bottom과 top에 대해서 각각 높이가 h일때에
# 쉽게 일관적으로 처리할 수 있었음
# 그릭고 여기서 h = 0 일수가 없으므로 또 인덱스 오류가 발생하지 않음
# 또 cnt = N //2로 한것은 어차피 초기에 는 H가 H이거나 0일 수 없으므로 h=1일때는 bot만 모두 포함이 되므로
# cnt = N //2 로처리한 것
# 생각보다 간단하지만
# 디테일이 많이 들어간 풀이
import sys
input = sys.stdin.readline

N, H = map(int, input().split())

tops = [0] * (H + 1)
bots = [0] * (H + 1)

for i in range(N):
    num = int(input())
    if i % 2 == 0:
        bots[num] += 1
    else:
        tops[H - num + 1] += 1

# solve
mn = int(1e12)
mn_num = 0

cnt = N // 2
for h in range(1, H + 1):
    cnt -= bots[h - 1]
    cnt += tops[h]

    if mn == cnt:
        mn_num += 1

    if mn > cnt:
        mn = cnt
        mn_num = 1

print(mn, mn_num)

# 세번째 풀이(강의 풀이))
# 시간 복잡도: (N*logN + H*logH)
# 풀이: 이분탐색을 이용한 풀이
# 리뷰
# 이분탐색에 대한 함수를 번영하지 않고도 푼 것
# 그리고 step방식으로 했을떄 같은 값이 들어가 있을때 최대 오른쪽에 있는 인덱스값을 가져오게 됨
import sys
input = sys.stdin.readline

def get_idx(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur + step] <= num:
            cur += step
        step //= 2

    return cur

# input
N, H = map(int, input().split())

tops = []
bots = []

for i in range(N):
    num = int(input())
    if i % 2 == 0:
        bots.append(num)
    else:
        tops.append(H - num + 1)


tops.sort()
bots.sort()

mn = int(1e12)
mn_num = 0

for h in range(1, H + 1):
    cnt_bot = (N // 2) - (get_idx(bots, h - 1) + 1)
    cnt_top = get_idx(tops, h) + 1

    if mn == cnt_bot + cnt_top:
        mn_num += 1

    if mn > cnt_bot + cnt_top:
        mn = cnt_bot + cnt_top
        mn_num = 1

print(mn, mn_num)

