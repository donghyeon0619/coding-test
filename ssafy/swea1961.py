"""
SWEA - 1961 숫자 배열 회전
Author: donghyeon
Date: 2026-07-03

[문제 요약]
    - N x N 정사각 행렬이 주어진다.
    - 이 행렬을 시계 방향으로 90도, 180도, 270도 회전시킨 세 가지 모양을 각각 구한다.
    - 출력 시 세 회전 결과를 한 줄에 나란히(사이에 공백 하나씩만 두고) 출력해야 한다.

[핵심 관찰]
    - 시계방향 90도 회전의 일반 공식은 after[i][j] = before[n - j - 1][i] 이다.
    - 180도, 270도는 별도로 공식을 유도할 필요 없이, 90도 회전을 결과에 반복 적용하면 얻어진다.
      (90도 회전 → 그 결과를 다시 90도 회전 = 180도 → 다시 90도 회전 = 270도)
    - 즉 "회전 함수 한 번만 정확히 만들고 그걸 누적 적용"하는 것이 핵심 아이디어.
    - 출력에서 각 행을 공백 없이 이어붙이는(''.join) 방식은 행렬 원소가 한 자릿수 숫자라는
      전제하에서만 안전하다 (이 문제의 입력 범위상 문제 없음).

[풀이 비교]
    풀이 1 :
        - rotate(before, n) 함수가 새로운 (n x n) 영행렬을 만들고,
          before[n-j-1][i] 공식으로 값을 채워 반환.
        - matrix → 90도 회전 → 180도 회전(90도 결과를 다시 90도 회전) → 270도 회전 순으로 누적 적용.
        - 출력 시 각 회전 행렬의 i번째 행을 문자열로 합친 뒤, print(a, end=" ") 세 번 호출로
          한 줄에 이어붙임.
        - (주석 처리된 대안) print(row_90, row_180, row_270)처럼 한 번의 print 호출에
          콤마로 넘기면 인자 사이에 자동으로 공백이 들어가므로 end=" "를 반복할 필요가 없어
          더 명확하지만, 로직상 동일한 결과.

    풀이 2 :
        - (미작성 - 예: zip(*matrix[::-1])을 이용한 반복문 없는 회전 등 대안 고려 시 추가)

[시간 복잡도]
    풀이 1: O(N^2) - 회전 함수 한 번 호출당 N x N 전체를 순회하며 값을 채움.
            세 번(90/180/270) 호출해도 상수배이므로 O(N^2)로 수렴.

[공간 복잡도]
    풀이 1 : O(N^2) - 회전마다 새 N x N 행렬을 생성 (matrix_90, matrix_180, matrix_270 총 3개 보유).

[복습 포인트]
    - "다음 회전 결과 = 이전 회전 결과에 같은 회전 함수를 한 번 더 적용"하는 패턴은
      회전 각도가 여러 개 필요한 문제에서 재사용 가치가 높다. (90도 공식만 정확히 알면
      180도, 270도, 360도까지 전부 커버 가능)
    - rotate 함수가 새 행렬을 만들어 반환하도록 짜면(참조를 안 밖에서 미리 만들지 않고),
      호출부가 matrix_90 = rotate(matrix, N)처럼 선언적으로 읽혀서 가독성이 좋아진다.

    - 원소가 한 자릿수라는 전제 하에 ''.join으로 붙이는 출력 방식은, 만약 원소가
      두 자릿수 이상이 될 수 있는 유사 문제를 풀 때는 통하지 않으므로 ' '.join 등으로
      바꿔야 한다는 점을 기억해두자.

"""
# 첫번쨰 풀이
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def rotate(before, n):
    after = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            after[i][j] = before[n - j - 1][i]
    return after


for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    matrix_90 = rotate(matrix, N)
    matrix_180 = rotate(matrix_90, N)
    matrix_270 = rotate(matrix_180, N)

    print(f"#{test_case}")

    for i in range(N):
        print(''.join(map(str, matrix_90[i])), end=" ")
        print(''.join(map(str, matrix_180[i])), end=" ")
        print(''.join(map(str, matrix_270[i])))
    # 같은 풀이
    # for i in range(N):
    #     row_90 = ''.join(map(str, matrix_90[i]))
    #     row_180 = ''.join(map(str, matrix_180[i]))
    #     row_270 = ''.join(map(str, matrix_270[i]))
    #     print(row_90, row_180, row_270)
    #








