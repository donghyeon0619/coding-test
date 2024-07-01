    ## 로또 문제
    ## 풀이 1 : 재귀함수를 이용
    ## 시간복잡도 : k의 범위의 끝을 n이라 했을 떄 최대 nC6이 걸림
    def combination(index, level):

        global choose, arr, k

        # base case
        if level == 6:
            for i in choose:
                print(i, end=' ')
            print()
            return

        # recursive
        for i in range(index, k):
            choose.append(arr[i])
            combination(i+1, level+1)
            choose.pop()


    while True:
        choose = []
        I = list(map(int, input().split()))

        k = I[0]
        arr = I[1:]

        if k == 0:
            break

        combination(0, 0)
        print()



## 풀이 2
## combination 함수를 이용
from itertools import combinations

while True:
    I = list(map(int, input().split()))

    k = I[0]
    arr = I[1:]

    if k == 0:
        break

    for comb in combinations(arr, 6):
        for u in comb:
            print(u, end=" ")
        print()
    print()


## 풀이 3
## 라이브러리인 combinations를 활용하면서 좀더 최적화 시킨 풀이
from itertools import combinations

while True:
    inputs = input()

    if inputs == '0':
        break
    else:
        arr = list(map(int,inputs.split()))[1:0]

        results = combinations(arr, 6)
        for result in results:
            print(str(result).replace(",", "")[1:-1])
        print()



