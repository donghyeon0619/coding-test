# 가장 긴 증가하는 부분수열
# 실버2
N = int(input())

arr = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = 1 + max(dp[j] for j in range(i) if arr[j] < arr[i])

print(max(dp))

# 두번쨰 풀이
# LIS 문제
# 이분탐색을 이용한
# patience sorting을 사용한 풀이
# 어려운 풀이 코딩테스트 수준에서는 안나올 꺼 같지만 이해만 하고 있어도 코드 퀄리티 면에서 올라갈 것 같음
def solution(ar):
    current = [0]

    for case in ar:
        if current[-1] < case:
            current.append(case)
        else:
            left = 0
            right = len(current)

            while left < right:
                mid = (left + right) // 2
                if current[mid] < case:
                    left = mid + 1
                else:
                    right = mid
            current[right] = case

    return len(current) - 1


N = int(input())
cases = map(int, input().split())

print(solution(cases))

# 세번째 풀이



