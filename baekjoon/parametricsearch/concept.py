"""
    파라매트릭 서치 알고리즘(매개 변수 탐색 알고리즘)

- 정의: 이분탐색을 이용하여 답을 구하는 알고리즘
- 특징
    - 최대값 최소값을 구하는 문제를 결정 문제로 바꾸어 푸는 알고리즘
    - 결정 문제(dicision problem: O/X로 답할 수 있는 질문형태)로 바꾸었을때, O/X 형태가
      "연속적"으로 나타나야 함
"""
# 방법 1
def parametric_search(arr):
    ret = -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid]:
            left = mid + 1
            ret = mid

        else:
            right = mid - 1

    return ret

arr = [True, True, True, True, True, True, True, True, False, False, False, False]
print(parametric_search(arr))

# 방법 2
def parametric_search(arr):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur + step]:
            cur += step
        step //= 2

    return cur


arr = [True, True, True, True, True, True, True, True, False, False, False, False]
print(parametric_search(arr))