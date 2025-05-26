# SWEA D2 문제
# 최대 이익 얻기
# 첫번쨰 풀이
# for문을 1부터 시작하는 것이 아닌 반댈로 마지막에 첫번째로 도는 풀이
# 수학에도 역함수가 있듯이 역으로 풀 수 있어야 함
import sys

readline = sys.stdin.readline
T = int(readline())
profits = []

for i in range(T):
    N = int(readline())
    max_price = 0
    profit = 0
    prices = [x for x in map(int, readline().split())]
    for j in range(N-1, -1, -1):
        if prices[j] > max_price:
            max_price = prices[j]
        else:
            profit += (max_price - prices[j])

    print(f"#{test_case} {profit}")

for i in range(T):
    print(f"#{i+1} {profits[i]}")
