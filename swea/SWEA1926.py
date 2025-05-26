# SWEA D2
# 간단한 369 게임
# 첫번째 풀이
# for문을 통한 간단한 풀이
# 범위가 10 이상이라 1~9까지는 하드코딩했지만 이것은 간단한 풀이
N = input()
digits = len(N)

num = ["3", "6", "9"]

print("1 2 - 4 5 - 7 8 -", end=" ")

for i in range(10, int(N)+1):
    list_i = list(str(i))
    count = sum(1 for x in list_i if x in num)
    if count == 0:
        print(i, end=" ")
    else:
        print("-"*count, end=" ")

# 두번째 풀이
# str을 list로 만들지 않고 str의 count()함수를 이용함
# 그리고 print()를 각각 내보내지 않고
# 정답 변수에 값을 다 담고 str으로 조인 후에 출력을 한번 함
# 이렇게 하면 i/o 시스템 호출을 최소화 하고 함수 호출도 최소화하므로 좀 더 나은 풀이
N = int(input())
res = []
for i in range(1, N+1):
    s = str(i)
    clap = s.count('3') + s.count('6') + s.count('9')
    if clap:
        res.append('-' * clap)
    else:
        res.append(s)

print(' '.join(res))


