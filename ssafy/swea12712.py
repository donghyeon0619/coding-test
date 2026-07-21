"""
SWEA - 12712 파리퇴치3
Author: donghyeon
Date: 2026-07-03

[문제 요약]


[핵심 관찰]


[풀이 비교]
    풀이 1 :


    풀이 2 :


[시간 복잡도]
    풀이 1:
[공간 복잡도]
    풀이 1 :

[복습 포인트]
    -
"""
# 첫번째 풀이

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    