# # 수 이어 쓰기2
# # 첫번쨰 풀이
# # 메모리 초과 발생. temp의 모든 int값을 넣게 되면 메모리 초과가 발생
# import sys
#
# readline = sys.stdin.readline
#
# N, k = map(int, readline().split())
#
# temp = []
#
# for i in range(1, N+1):
#     temp.append(i)
#
# numStr = "".join(str(s) for s in temp)
#
# if k > len(numStr):
#     print(-1)
# else:
#     print(numStr[k-1])
#
#

# 두번쨰 풀이
# 자릿수 구하는 공식도 잘못됬고 범위를 구한 것도 잘못됨
# 그리고 총자릿수를 구하는 것보단 k를 줄여가면서 구하는 것이 가장 적절한 풀이
# N, k = input().split()
# k = int(k)
# N_len = len(N)
# order = 0
#
#
# # 수의 길이 구하기
# if len(N) == 1:
#     order = int(N)
# else:
#     for i in range(1, N_len + 1):
#         if i == N_len:
#             for _ in range(1, int(N[i - N_len])):
#                 order += i * 10
#             order += int(N[1:]) + 1
#         else:
#             order += 9 * i * 10 ** (i - 1)
#
# if order < k:
#     print(-1)
# else:
#     for i in range(1, N_len+1):
#         if k - 9 * i * 10 ** (i - 1) < 0:
#             if k % i == 0:
#                 num = 10 ** (i-1) + (k // i) - 1
#                 print(str(num)[-1])
#             else:
#                 num = 10 ** (i-1) + (k // i)
#                 print(str(num)[k % i])
#         else:
#             k -= 9 * i * 10 ** (i-1)


# 세번째 풀이
# 단순히 수를 모두 이어 붙혀 문자열을 만들고 문자열의 K번쨰 수를 출력하면 될 것 같지만 n이 최대 1억개라
# 이어붙이는 과정에서 메모리 초과가 발생할 수 있음
# 그렇기 떄문에 이어붙이는게 아닌 탐색을 해야함
# 몇번째 수를 구하는 문제이므로 "자릿수"가 중요

import sys
readline = sys.stdin.readline

N, k = map(int, readline().split())

length = 1
start = 1 # 해당 자릿수 구간의 첫 숫자
while True:
    end = min(N, 10**length - 1)
    cnt = end - start + 1   # 이 자릿수 구간에 실제로 들어 있는 숫자 개수
    digits = cnt * length   # 이 구간에 차지하는 전체 자리수

    if k > digits:  # k가 아직 뒤에 있다 -> k를 줄이고 다음 자릿수로
        k -= digits
        length += 1
        start = 10 ** (length-1)
        if start > N:   # 모든 숫자를 다 써도 k를 못채움
            print(-1)
            break

    else:   # 답이 이 구간 안에 있음
        num_index = (k - 1) // length   # 몇 번쨰 숫자인지 여기서 "k-1"은 숫자가 0부터 시작하므로
        digit_index = (k - 1) % length  # 그 숫자의 몇 번쨰 자리인지
        number = start + num_index
        print(str(number)[digit_index])
        break

# 4번째 풀이
N, k = map(int, input().split())

start = 0
digit = 1
nine = 9

while k > nine * digit:
  k = k - (digit * nine)
  start = start + nine
  nine = nine * 10
  digit += 1

result = (start + 1) + (k - 1) // digit

if result > N:
    print(-1)
else:
    print(str(result)[(k-1) % digit])






