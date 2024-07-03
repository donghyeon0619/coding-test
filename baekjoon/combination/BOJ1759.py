## 암호 만들기 (못풀었으므로 다시 풀어보기)
## 2024.07.03
## 풀이1: 조합 알고리즘을 이용해서 풀기(직접 구현)
## 시간 복잡도: O(cCl)
vowels = ['a', 'e', 'i', 'o', '']   # 모음 집합이고 모음 문제가 나왔을때 모음을 이용하는 것을 생각하는게 좋은 듯
choose = []


def is_possible():
    global L, C, choose, arr

    vow = 0
    for c in choose:
        vow += (c in vowels)    # True일 경우 1로 매핑됨
    con = L - vow

    return vow >= 1 and con >= 2


def combination(idx, lev):
    global L, C, choose, arr

    # base case
    if lev == L:
        if is_possible():
            print(''.join(choose))
        return

    # recursive case
    for i in range(idx, C):
        choose.append(arr[i])
        combination(i+1, lev+1)
        choose.pop()


L, C = map(int, input().split())
arr = input().split()

arr.sort()

combination(0, 0)



## 풀이2: combination 라이브러리를 이용한 풀이
## 시간 복잡도: O(cCl)
from itertools import combinations

vows = ['a', 'e', 'i', 'o', 'u']


def is_possible(word):
    global L, C, arr

    vow = 0
    for w in word:
        vow += (w in vows)
    con = L - vow

    return vow >= 1 and con >= 2


L, C = map(int, input().split())
arr = input().split()

arr.sort()

for word in combinations(arr, L):
    if is_possible(word):
        print(''.join(word))


