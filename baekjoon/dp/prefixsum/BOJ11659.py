# 구간 합 구하기 4
# 실버 3
# 첫번째 풀이
# 누적합을 이용하여 1차원 배열 누적합 배열을 구함
# 함수를 정의해서 해도 되지만
# 출력횟수가 많아진다면 함수를 호출하는 비용이 늘게 되고 그에 따른 실행속도도 늘어남
# 그리고 print()문도 출력횟수 만큼 반복하는 것 보다는 prefix sum값을 구하고 그 값을 출력변수에 넣고 나서
# 한번에 출력하는 방식으로 하는 것이 적절
import sys

input = sys.stdin.readline

# def get_sum(a, b):
#     global psum
#     return psum[b] - psum[a-1]


N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

psum = [0] * (N + 1)
for n in range(1, N + 1):
    psum[n] = psum[n - 1] + arr[n]

result = []
for _ in range(M):
    i, j = map(int, input().split())
    result.append(str(psum[j] - psum[i-1]))

print('\n'.join(result))

e


