## 칸토어 집합 문제 ##
## 풀이 1: bottom-up 방식
## 시간 복잡도 : O(3^n)
ans = [''for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + (' '*(3**(i-1))) + ans[i-1]


while True:
    try:
        N = int(input())
        print(ans[N])
    except EOFError:
        break


## 풀이 2: 재귀함수 이용
## 시간 복잡도 : O(3^n)
def func(k):
    # base case
    if k == 0:
        print('-', end="")
        return

    # recursive case
    func(k-1)
    print(" "*3**(k-1), end="")
    func(k-1)


while True:
    try:
        N = int(input())
        func(N)
        print()

    except EOFError:
        break

