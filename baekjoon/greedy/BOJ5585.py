# 거스름돈 풀아
# 첫번째 풀이
# for문을 사용하지 않은 간단한 풀이
total = 1000
price = int(input())

x = total - price

cnt = 0

cnt += (x // 500)
x %= 500

cnt += (x // 100)
x %= 100

cnt += (x // 50)
x %= 50

cnt += (x // 10)
x %= 10

cnt += (x // 5)
x %= 5

cnt += (x // 1)
x %= 1

print(cnt)

# 두번째 풀이
# for문을 이용하고 잔돈 변수를 하나 설정해서 풀음
total = 1000

price = int(input())
cnt = 0
coins = [500, 100, 50, 10, 5, 1]

x = total - price

for i in coins:
    cnt += x // i
    x %= i

print(cnt)

