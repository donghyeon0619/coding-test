"""
SWEA - 1959 두개의 숫자열
Author: donghyeon
Date: 2026-07-03

[문제 요약]
    - N개의 숫자로 이루어진 수열 Ai와 M개의 숫자로 이루어진 수열 Bj가 주어진다.
    - 짧은 쪽 수열을 긴 쪽 수열 위에서 좌우로 움직여(단, 긴 쪽의 양 끝을 벗어나지 않는 범위 내에서)
      서로 마주보는 위치의 숫자끼리 곱한 값을 모두 더한다.
    - 가능한 모든 위치 중 이 합이 최대가 되는 값을 구한다.

[핵심 관찰]
    - N, M ≤ 20 이라는 작은 제약 덕분에 완전탐색으로 모든 슬라이딩 위치를 다 확인해도 충분하다.
    - 두 수열 중 짧은 쪽을 고정 길이로 놓고, 긴 쪽 위에서 (l_len - s_len + 1)번만 슬라이딩하면 되므로
      "누가 짧고 누가 긴지"만 먼저 구분해주면 로직은 하나로 통일할 수 있다.
    - 즉 핵심은 슬라이딩 윈도우(sliding window) + 내적(dot product) 계산.

[풀이 비교]
    풀이 1 :
        - 짧은 수열/긴 수열을 구분한 뒤, 이중 for문으로 직접 인덱스(i + j)를 계산해 곱의 합을 구함.
        - 로직이 명시적으로 드러나 이해하기 쉽지만 인덱스 계산을 직접 다뤄야 함.

    풀이 2 :
        - 풀이 1과 동일한 로직이나, 내부 곱셈-합산 부분을 zip + sum으로 대체.
        - long_arr[i:i+s_len] 슬라이싱과 zip을 이용해 인덱스 연산 없이 대응되는 원소끼리 곱해서 더함.
        - 가독성은 좋아지지만 매 반복마다 슬라이스로 새 리스트를 생성하므로 미세한 오버헤드가 있음
          (단, N, M ≤ 20이라 실질적 성능 차이는 없음).

[시간 복잡도]
    풀이 1: O((l_len - s_len + 1) * s_len)  → 최악의 경우 O(N*M), N,M ≤ 20이므로 최대 20*20 수준
    풀이 2: 풀이 1과 동일 O((l_len - s_len + 1) * s_len), 슬라이싱 비용 O(s_len)이 추가되나 점근적으로는 동일

[공간 복잡도]
    풀이 1 : O(N + M)  (입력 배열 저장 외 추가 공간 거의 없음)
    풀이 2 : O(N + M) + 슬라이딩마다 임시 슬라이스 O(s_len) 생성 (즉시 소멸되어 누적되지는 않음)

[복습 포인트]
    - best를 0으로 초기화했는데, 만약 입력에 음수가 포함되어 모든 슬라이딩 위치의 합이 음수가 되는
      경우가 있다면 오답(0 반환) 가능성이 있음. 이번 문제에서는 통과했지만 일반화된 문제라면
      best = float('-inf') 또는 None으로 초기화하는 습관을 들이자.
    - zip(small_arr, long_arr[i:i+s_len]) 패턴은 "두 수열의 대응 원소를 곱해서 더하는" 문제에서
      자주 쓰이는 파이썬 관용구이니 익혀두면 좋다.
    - 짧은/긴 배열을 미리 정렬(구분)해서 하나의 함수로 처리하는 패턴 자체도 재사용성이 높다.

"""
# 첫번째 풀이
T = int(input())

def solve(small_arr, big_arr, s_len, l_len):

    best = 0

    for i in range(0, l_len - s_len + 1):
        num = 0
        for j in range(0, s_len):
            num += small_arr[j] * big_arr[i + j]

        best = max(num, best)

    return best


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    answer = 0

    if N < M:
        answer = solve(Ai, Bj, N, M)
    else:
        answer = solve(Bj, Ai, M, N)

    print(f"#{test_case} {answer}")



# 두번쨰 풀이
# 좀더 파이썬 스럽게 푼 풀이
T = int(input())

def solve(small_arr, long_arr, s_len, l_len):

    best = 0

    for i in range(l_len - s_len + 1):
        num = sum(a * b for a, b in zip(small_arr, long_arr[i:i+s_len]))
        best = max(num, best)
    return best


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    answer = 0

    if N < M:
        answer = solve(Ai, Bj, N, M)
    else:
        answer = solve(Bj, Ai, M, N)

    print(f"#{test_case} {answer}")