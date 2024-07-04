# 순열 알고리즘 개념
# : n개의 원소중에서 r개를 나열하는 모든 경우를 살펴보는 알고리즘
# for문을 이용해서 구현하는 것 보단 재귀함수를 이용하는 것이 효율적이다.
# 시간복잡도 O(nPr)임

N = 10
R = 3
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
check = [False] * N
# check[k]가 true이면 인덱스가 k인 원소가 사용중임을 나타냄
# check[k]가 false이면 인덱스가 k인 원소가 사용중이지 않음을 나타냄
choose = []     # 나열한 원소를 보관


def permutation(level):
    if level == R:
        # 나열한 R개의 원소 출력
        print(choose)
        return

    # for문
    for i in range(0, N):
        if check[i] == True:    # 인덱스가 i인 원소가 이미 사용중이라면 continue
            continue

        choose.append(lst[i])   # 인덱스가 i인 원소를 선택(추가)
        check[i] = True     # 인덱스가 i인 원소를 사용하고 있으므로 true값으로 초기화

        permutation(level+1)    # 다음 for문으로 들어가는 역할

        check[i] = False    # 인덱스가 i인 원소의 사용이 끝났으므로 false로 초기화
        choose.pop()    # (넣었던) 인덱스가 i인 원소를 제거


permutation(0)




