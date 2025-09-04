"""
    이분탐색 알고리즘: 정렬된 배열에서 특정한 원소를 찾는 알고리즘

- 특징: 정렬된 배열이 아니라면 사용할 수 없음
- 선형탐색 vs 이분탐색
    - 선형 탐색
        - 특정한 원소를 선형 탐색으로 찾는다면, O(N)의 시간복잡도가 걸림
        - 정렬이 되어 있지 않은 상태에서도 사용 가능하다
    - 이분 탐색
        - 특정한 원소를 이분탐색으로 찾는다면, O(logN)의 시간 복잡도가 걸림
        - 정렬이 된 상태에서만 가능함

    - 정렬이 되어 있지 않은 상태에서 "특정한 원소"를 찾을때
        1) 선형 탐색
            : O(N)
        2) 정렬을 하고 이분 탐색
            : O(NlogN) + O(logN)
        -> 즉, 특정한 원소를 찾을때는 선형 탐색이 이득임
    - 정렬이 되어 있지 않은 상태에서 "특정한 원소 M개"를 찾을때
        1) 선형 탐색
            : O(N) * O(M) = O (MN)
        2) 이분 탐색
            : O(NlogN) + O(MlogN) = O(NlogN)
        -> 즉, 특정한 원소 M개를 찾을때는 이분탐색이 이득
"""
# 첫번째 방법
# 시간복잡도: O(logN)
# 특징
# - left와 right 변수를 통해서, 원소의 범위를 좁혀나가는 방식
# - 종료 조건: left > right
def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < num:
            left = mid + 1

        if arr[mid] > num:
            right = mid - 1

        if arr[mid] == num:
            return mid

    return -1

print(binary_search([1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 13, 16], 10))

# 두번쨰 방법
# 시간복잡도: O(logN)
# 특징
# - 현재 위치 cur와 탐색할 보폭 step을 이용해서, 원소를 찾아가는 방식(파라매트릭 서치 알고리즘에서 많이 사용됨)
# - 종료 조건 step == 0
def binary_search(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur + step] <= num:
            cur += step

        step //= 2

    return cur

print(binary_search([1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 13, 16], 10))