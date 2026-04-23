"""
Programmers - 두 큐 합 같게 만들기
난이도: Essential
분류: 투 포인터, 큐, 시뮬레이션

Author: donghyeon
Date: 2026-04-23

[문제 요약]
- 길이가 같은 두 큐가 주어진다.
- 한 큐의 맨 앞 원소를 꺼내 다른 큐의 맨 뒤에 넣는 작업을 반복하여
  두 큐의 원소 합을 같게 만들고자 한다.
- 필요한 최소 작업 횟수를 구하고, 만들 수 없으면 -1을 반환한다.

[핵심 관찰]
1. 두 큐의 전체 합이 홀수라면, 두 큐의 합을 같게 만들 수 없다.
2. 목표값은 target = (sum(queue1) + sum(queue2)) // 2 이다.
3. queue1의 합만 target으로 맞추면 queue2의 합도 자동으로 target이 된다.
4. 이 문제는 실제 큐 연산을 직접 수행해도 되지만,
   queue1 + queue2를 하나의 배열로 보고 queue1을 연속 구간으로 해석할 수도 있다.

[풀이 비교]
1. 첫 번째 풀이
   - merged 배열 위에서 queue1을 하나의 연속 구간으로 보고 투 포인터로 접근
   - 종료 조건이 다소 구현 의존적임

2. 두 번째 풀이
   - 첫 번째 풀이를 리팩토링한 버전
   - 이동 횟수 상한(limit)을 두어 종료 조건을 더 명확하게 구성

3. 세 번째 풀이
   - deque를 사용해 실제 큐 연산을 그대로 수행
   - 문제 설명에 가장 직접적으로 대응되는 풀이
   - 본질적으로는 첫 번째/두 번째 풀이와 같은 상태 변화를 만든다

[시간 복잡도]
- 첫 번째, 두 번째, 세 번째 풀이 모두 O(n)

[공간 복잡도]
- 첫 번째, 두 번째 풀이: O(n)  (merged 배열 사용)
- 세 번째 풀이: O(n)  (deque 사용)
"""

# -------------------------------------------------------------------
# 1. 첫 번째 풀이
# -------------------------------------------------------------------
# [풀이 복기]
# - queue1 + queue2 를 하나의 배열(merged)로 합친다.
# - 현재 queue1이 merged 위에서 차지하는 연속 구간을 [left, right]로 본다.
# - sum1 > target 이면 queue1의 앞 원소를 제거하는 것과 같으므로 left를 이동한다.
# - sum1 < target 이면 queue2의 앞 원소를 받아오는 것과 같으므로 right를 이동한다.
# - 다만 종료 조건이 left <= right, right 경계 체크에 의존해 있어
#   논리적으로 조금 덜 명확할 수 있다.
def solution_v1(queue1, queue2):

    sum1 = sum(queue1)
    total_sum = sum1 + sum(queue2)

    if total_sum % 2 == 1:
        return -1

    target = total_sum // 2

    moves = 0
    merged = queue1 + queue2
    left = 0
    right = len(queue1) - 1
    while left <= right:
        if sum1 == target:
            return moves

        if sum1 > target:
            sum1 -= merged[left]
            left += 1
        else:
            if right == len(merged) - 1:
                break
            right += 1
            sum1 += merged[right]

        moves += 1

    return -1

# -------------------------------------------------------------------
# 2. 두 번째 풀이 (리팩토링)
# -------------------------------------------------------------------
# [개선 포인트]
# - 첫 번째 풀이의 아이디어는 유지한다.
# - 다만 종료 조건을 단순한 구간 모양(left <= right)에 맡기지 않고,
#   최대 이동 횟수(limit)를 두어 더 본질적으로 제어한다.
# - 현재 구현에서는 merged 범위를 벗어나는 것을 막기 위한
#   인덱스 보호 조건도 함께 둔다.
def solution_v2(queue1, queue2):

    sum1 = sum(queue1)
    n1 = len(queue1)
    total_sum = sum1 + sum(queue2)

    if total_sum % 2 == 1:
        return -1

    target = total_sum // 2

    moves = 0
    merged = queue1 + queue2
    left = 0
    right = n1 - 1
    limit = n1 * 3
    while moves < limit:
        if sum1 == target:
            return moves

        if sum1 > target:
            sum1 -= merged[left]
            left += 1
        else:
            if right + 1 >= len(merged):
                return -1
            right += 1
            sum1 += merged[right]

        moves += 1

    return -1

# -------------------------------------------------------------------
# 3. 세 번째 풀이 (deque 풀이)
# -------------------------------------------------------------------
# [풀이 복기]
# - 실제 큐 연산을 deque로 그대로 구현한다.
# - 합이 더 큰 큐의 앞 원소를 꺼내, 합이 더 작은 큐의 뒤에 붙인다.
# - 한 번에 여러 개를 옮기는 것이 아니라, 원소 1개씩 이동 후 다시 판단한다.
# - limit를 두어 불가능한 경우 무한 반복을 방지한다.
# - 표현 방식은 다르지만, 상태 변화 자체는 투 포인터 풀이와 본질적으로 같다.
from collections import deque


def solution_v3(queue1, queue2):
    main_que, sub_que = deque(queue1), deque(queue2)

    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        return -1
    target = total // 2

    limit = 4 * len(main_que)
    main_sum = sum(main_que)
    for cnt in range(limit):
        if main_sum == target:
            return cnt
        elif main_sum < target:
            val = sub_que.popleft()
            main_sum += val
            main_que.append(val)
        else:
            val = main_que.popleft()
            main_sum -= val
            sub_que.append(val)

    return -1

