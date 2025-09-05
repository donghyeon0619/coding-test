"""
문제: 수 찾기
수준: 실버 4
"""
# 첫번째 풀이 (내 풀이)
# 이분탐색 방법을 사용해서 풀음
# 근데 해시함수를 이용한 set 이용해서 찾는것도 나쁘지 않은 듯
def binary_search(a, num):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] < num:
            left = mid + 1
        if a[mid] > num:
            right = mid - 1
        if a[mid] == num:
            return 1

    return 0


N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
arr = list(map(int, input().split()))

for m in range(M):
    arr[m] = binary_search(A, arr[m])

print(*arr, sep="\n")

# 두번쨰 풀이
# 리스트 컴프리핸션을 이용한 간단한 풀이
# 이런 어떤 값을 찾을때는 SET 자료구조를 이용하는 것이 가장 효율적
N = int(input())
A = set(input().split())
M = int(input())
print('\n'.join(["1" if num in A else "0" for num in input().split()]))



