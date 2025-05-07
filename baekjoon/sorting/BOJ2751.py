# 수 정렬하기 2

import sys

readline = sys.stdin.readline

N = int(readline())
num = []

for _ in range(N):
    num.append(int(readline()))

s_num = sorted(num)

print('\n'.join(map(str, s_num)))


# 두번쨰 풀이
# 정렬을 이용하지 않고 카운팅 소트를 이용함
def sol():
    a = [None]*2000001
    b = map(int, open(0))
    next(b)
    for i in b:
        a[i] = 1
        print("\n".join(str(i) for i in range(-1000000, 1000001, 1) if a[i]))


sol()
