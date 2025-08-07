"""
문제: 2xn 타일링
난이도: 실버3
중요도: 별*5
"""
# 첫번째 풀이
# 맞추긴 했지만 if문을 써서 코드 퀄리티가 애매함
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n-1] % 10007)

# 두번쨰 풀이
# 로직은 똑같으면서 좀더 인덱스 오류라는 것들에 대해서 좀 더 효율적으로 풀이한 풀이

n = int(input())
dp = [1] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n] % 10007)

# 세번째 풀이 (강의풀이) (bottom-up 방식)
# 답을 구하고나서 나머지를 구하는 것이 아닌 답을 구하는 과정에서 mod(나머지)연산을 진행하는 방법
# 문제를 제출했을 때 시간이 오래 걸렸던 이유가
# 큰 값을 연산해서 계산이 오래 걸렸던 것이였음
# 문제에서 "어떤 수를 k로 나눈 나머지를 출력하라"라는 내용이 들어가 있다면,
# 보통 dp 문제이고 그리고 구하는 값이 너무 크므로 출력할 수 없다는 것을 의미함
#
N = int(input())

# solve
dp = [0] * (N + 2)
dp[1] = 1
dp[2] = 2

for n in range(3, N + 1):
    dp[n] = (dp[n-1] + dp[n-2]) % 10007

print(dp[N])

# 네번째 풀이(강의 풀이)(top-down 방식)
import sys
sys.setrecursionlimit(int(1e6))


def func(n):
    global dp

    # base case
    if n == 1 or n == 2:
        return n
    if dp[n] != -1:
        return dp[n]

    # recursive case
    dp[n] = (func(n-1) + func(n-2)) % 10007

    return dp[n]

# input
N = int(input())

# solve
dp = [-1] * (N + 1)

print(func(N))
