# 도서관
# 골드 4
# 첫번쨰 풀이(실패)
# 이 문제는 브루트 포스로는 풀 수가 없음
# 처음에어떻게 풀어야하는지 생각은 했지만 구현은 못함
# 느낌상 배열을 두개 만들고 정렬을 두번하는것이 좋아보이는것 까지는 생각해냄
# 그래서 두가지 배열을 만들고 이에대해서 구현하는 것을 해결
# 인덱스 오류가 발생했을때가 떳는데 에러 케이스 생각하는 습관 들이기

N, M = map(int, input().split())
books = sorted(list(map(int, input().split())))

sum = 0
max_sign = 1
neg_num = []
pos_num = []

for i in range(len(books)):
    if books[i] < 0:
        neg_num.append(books[i])
    else:
        pos_num.append(books[i])

if neg_num and not pos_num:
    max_sign = 0
elif not neg_num and pos_num:
    max_sign = 1
elif abs(neg_num[0]) > pos_num[-1]:
    max_sign = 0

if neg_num:
    for i in range(0, len(neg_num), M):
        if i == 0 and not max_sign:
            sum += abs(neg_num[i])
        else:
            sum += abs(neg_num[i]) * 2

if pos_num:
    for i in range(len(pos_num)-1, -1, -M):
        if i == len(pos_num)-1 and max_sign:
            sum += pos_num[i]
        else:
            sum += pos_num[i] * 2

print(sum)

## 두번째 풀이
## 내 풀이에서 좀 더 간결하고 직관적으로 잘 푼 풀이
## 그리고 이동거리를 하나에 배열에 담아놓고 거기서 max를 이용해서 가장 큰 값만 한번 구하는 식으로 구현
## 어차피 이동거리는 양수이므로 하나에 담아도 되고 문제를 분석했을 때 가장 큰값만 한번 더하는 식이라 상관 없음
## 그리고 값들을 더한 다음에 max 값은 한번만 더해야하므로 역으로 max를 한번 뺴줌
N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))

answer = []

pos = []
neg = []

for i in arr:
    if i > 0:
        pos.append(i)
    else:
        neg.append(-i)

sorted1 = sorted(pos)[::-1]
sorted2 = sorted(neg)[::-1]

## M만큼 떨어진 요소만 슬라이싱으로 담금으로 이 값들을 더해주면 됨
for i in sorted1[::M]:
    answer.append(i)
for j in sorted2[::M]:
    answer.append(j)

print((2 * sum(answer)) - max(answer))
