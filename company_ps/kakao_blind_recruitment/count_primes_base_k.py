# k진수에서 소수 개수 구하기
# 문제를 잘 이해할 수 있어야 할듯(많이 풀어야 할 것 같다, 책도 많이 보고 평소에)
# 소수 관련 문제를 다뤄본적이 없었는데, 이번기회에 다뤄보게 된것같고
# 그리고 spilt()함수에 돌아가는 방식에 대해서 다시한번 생각해볼 수 있는 문제였다
# 그리고 십진수에서 k진수 넘어가는 방법에 대한 코드를 처음 접하게 됨
# 이 문제에 시간복잡도도 구할줄 아는게 좋을듯 최악의 경우 O(1000만)임
from math import sqrt

def solution(n, k):
    answer = 0

    n_to_k = dec_to_k(n, k)
    k_list = [int(x) for x in n_to_k.split("0") if x]

    for num in k_list:
        if is_prime(num):
            answer += 1

    return answer


def is_prime(num):
    s = set()
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            s.add(i)
            s.add(num // i)

    return True if len(s) == 2 else False


def dec_to_k(num, k):
    k_num = ""

    while num != 0:
        value = num % k
        k_num = str(value) + k_num
        num //= k

    return k_num

## 두번째 풀이
## 좀더 최적화한 방식
## 작은 수에 범위라 상관없지만 더 안전한 방식을 위해서
## 큰 수/엄밀성 측면에서 isqrt를 사용
## 그리고 value를 나눠서 해당 값이 문자열로 변환하고 하는 것은 비용면에서 많이 들 수 있으므로 일단 배열의 저장하고
## reverse 한다음에 한번에 문자열로 변환해서 반환하는 것이 적절
from math import isqrt

def solution(n, k):
    n_to_k = dec_to_k(n, k)
    answer = 0

    for part in n_to_k.split("0"):
        if part and is_prime(int(part)):
            answer += 1

    return answer

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    r = isqrt(num)
    for i in range(3, r + 1, 2):
        if num % i == 0:
            return False
    return True

def dec_to_k(num, k):
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(str(num % k))
        num //= k
    return ''.join(reversed(digits))

## 세번째 풀이 (강의풀이)
## 위에랑 비슷한 풀이
## 다른거라면 sqrt()함수를 쓰지 않았고, 그리고 set()함수도 쓰지않고 그냥 flag만 보내주도록 함

def convert(num, k):
    ret = ""

    while num != 0:
        ret = str(num % k) + ret
        num //= k

    return ret

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def solution(n, k):
    num_string = convert(n, k)
    nums = num_string.split('0')

    ans = 0
    for num in nums:
        if num != '':
            ans += is_prime(int(num))

    return ans