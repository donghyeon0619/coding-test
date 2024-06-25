##  피보나치 수(5) 구하기    ##

# 풀이 1 : 반복문 + 메모이제이션
# 시간복잡도 : O(n)
n = int(input())

arr = [-1] * (n+2)  # n+1이 아닌 n+2로 한 이유는 n=2일 때 arr[1]에 접근할 수 있도록 하기 위해서 이다.
arr[0] = 0          # -1 은 '값이 갱신되지 않음'을 의미하는데 피보나치의 수에서 -1이 없기 떄문에 사용 가능
arr[1] = 1

for i in range(2, n+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])


# 풀이 2 : 재귀함수
# 시간복잡도 : O(2^n)
# 재귀함수에서는 함수를 두번 호출하면 연산횟수가 많아지게 되는데
# 왜냐하면 x = 20 을 했을 떄 재귀 도중에 fibo(18)이 두 번 실행되는 것을 알 수 있음
def fibo(x):
    # base case
    if x <= 1:
        return x
    # recursive case
    else:
        return fibo(x-1) + fibo(x-2)


n = int(input())
print(fibo(n))


# 풀이 3 : 재귀함수 + 메모이제이션
# 시간복잡도 : O(n)
# n값이 엄청 컸을때 재귀함수로 하는 것보다 더 단축될 껏 같다.
def fibo(x):
    global arr

    # base case
    if arr[x] != -1:
        return arr[x]

    # recursive case
    arr[x] = fibo(x-1) + fibo(x-2)
    return arr[x]


n = int(input())
arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

print(fibo(n))

# 참고
# 메모이제이션 기법 : 이미 계산한 값을 저장해둠으로써 불필요한 중복 계산을 막는 방법
# 이 풀이들로 백준 피보나치 수 (3) 을 풀어보면 런타임에러 나 메모리 초과가 나옴
# 그렇기 때문에 이 풀이들이 피보나치 수 문제에 다 적용되는 건 아니므로 n이 많아질 떄는 따로 고민이 필요

