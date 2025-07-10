# 보물
# 실버 4
# 첫번째 풀이(성공)
# 문제에서는 "B에 있는 수는 재배열하면 안된다"고 했지만, 배열 2개를 모두 재배열 할 수 있다고 생각해도 무방함
# 왜냐하면 "A와 B를 모두 재배열해서 나올 수 있는 경우"는 "A만 재배열하는 경우"에도 나올 수 있으므로
N = int(input())

A = sorted(list(map(int, input().split())))
# 똑같은 역순 만들기
# sorted(list(map(int, input().split())), reverse=True)[::-1]
B = sorted(list(map(int, input().split())), reverse=True)

min = 0

for i in range(N):
    min += A[i] * B[i]
# zip()함수를 이용해서 같은 것 끼리 묶을 수 있음
# 여기서 zip()함수는 크기가 같은 리스트(iterable(반복가능한 객체))를 넣으면 인덱스별로 묶어서 반환해줌
# for a, b in zip(A, B):
#     min += a *b

print(min)




