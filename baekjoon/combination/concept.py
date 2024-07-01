# 조합 알고리즘 개념

## 첫번째 for문을 이용한 조합 알고리즘 구현
## 1~11의 11개의 원소중에서 3개를 선택하는 모든 경우를 살펴보는 코드
# for i in range(1, 11+1):
#     for j in range(i+1, 11+1):
#         for k in range(j+1, 11+1):
#             # {i, j , k}를 선택


## for문으로 해야할 때 만약에 5개를 뽑게되면 5중 for문을 만들어야하므로 비효율적임
## -> 재귀함수를 이용해서 구현 하는것이 가장 일반적
## 재귀 함수를 이용한 조합 알고리즘 구현
N = 10
R = 5
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
choose = []


def combination(index, level):

    # base case
    if level == R:
        print(choose)
        return

    # recursive case
    for i in range(index, N):
        choose.append(lst[i])   # 인덱스가 i인 원소를 선택(추가)
        combination(i+1, level+1)   # 다음 for문으로 들어가는 상황
        choose.pop()


combination(0, 0)
