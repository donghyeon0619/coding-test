## 모든 순열 문제
## 2024.07.05
## 백준 문제를 풀때는 출력되는 형식(ex. 데이터사이에 빈칸 갯수 등)도 고려를 해서 풀어야 함
## 풀이 1 : 직접 알고리즘을 구현
def permutation(level):
    global n, check, choose

    ## base case
    if level == n:
        # print(str(choose).replace(",", "")[1:-1]) 같은 의미 인데 아래가 더 간단해보임
        print(" ".join(map(str, choose)))
        return

    ## recursive case
    # for i in range(n):
    #     if not check[i]:
    #         choose.append(i + 1)
    #         check[i] = True
    #
    #         permutation(level + 1)
    #         check[i] = False
    #         choose.pop()

    # for에서 n+1로 하는 것이 한번만 계산이 되므로 엄청 큰차이는 없어 보이지만 이 아래같이 쓰는 것이 좀 더 단축시킬 수 있음
    for i in range(1, N + 1):
        if check[i] == True:
            continue

        choose.append(i)
        check[i] = True

        permutation(level + 1)

        check[i] = False
        choose.pop()


n = int(input())
# check = [False] * n
check = [False] * (n + 1)
choose = []

permutation(0)



## 두번쨰 풀이 : 라이브러리 이용
from itertools import permutations

    n = int(input())

for perm in permutations(range(1, n+1)):
    print(" ".join(map(str, perm)))



## 세번째 풀이 : 가장 빠른 실행시간이 나오는 풀이이고 직관적임
## permutations()는 문자열도 순열을 만들어줄 수 있음
from itertools import permutations
print("\n".join(map(" ".join, permutations(map(str, range(1, int(input()) + 1))))))
