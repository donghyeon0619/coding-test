# SWEA D2 문제
# 파리 문제
# 첫번째 풀이(틀린 풀이)
# for문을 이용했지만 for문을 비효율적으로 이용한 풀이

# T = int(input())
#
#
# def sum_kill_flies(s_r, s_c, e_r, e_c):
#     cnt = 0
#     for i in range(s_r, e_r):
#         for j in range(s_c, e_c):
#             cnt += flies[i][j]
#
#     return cnt
#
#
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     flies = [list(map(int, input().split())) for _ in range(N)]
#     kill_flies = []
#     start_raw = 0
#     start_col = 0
#     end_raw = M
#     end_col = M
#     num = (N - M + 1)**2
#
#     while True:
#         kill_flies.append(sum_kill_flies(start_raw, start_col, end_raw, end_col))
#         if end_raw >= N and end_col >= N:
#             break
#         elif end_col < N:
#             start_col += 1
#             end_col += 1
#             continue
#         else:
#             start_raw += 1
#             end_raw += 1
#             start_col = 0
#             end_col = M
#
#     print(f"#{t} {max(kill_flies)}")


# 두번쨰 풀이
# for문을 중복해서 푼 풀이(첫번째 풀이보다 가독성이 좋음)
# 이 풀이는 값을 구하고 나서 배열을 새로 생성하여 그 안에 넣는 것이고 마지막에 max()를 이용하는 방법이 아닌
# 루프를 돌때마다 최선의 max값을 추출해서 변수에 넣으므로 좀더 최적화된 풀이
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            # 그안을 2중 루프로 순회하여  환산
            for di in range(M):
                for dj in range(M):
                    s += flies[i + di][j + dj]
            # 최대값 갱신
            if s > best:
                best = s

    print(f"#{t} {best}")

# 세번쨰 풀이
# 누적합(prefix sum)을 이용한 풀이
# 이 풀이는 N의 범위가 넓어졌을 떄 유용함
# 그리고 단순한 누적합 풀이가 아닌 2d 즉, 2차원 배열을 이용한 누적합 풀이

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    # 1) (N+1) * (N+1) 크기의 누적합 배열 초기화
    ps = [0 * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        row_sum = 0
        for j in range(1, N+1):
            row_sum += flies[i-1][j-1]
            ps[i][j] = ps[i-1][j] + row_sum


    # 2) 블록합을 O(1)로 계산하여 최대값 찾기
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = (
                ps[i+M][j+M]
                - ps[i][j+M]
                - ps[i+M][j]
                + ps[i][j]
            )
            if total > best:
                best = total

    print(f"#{t} {best}")




