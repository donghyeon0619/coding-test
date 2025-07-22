# 누적합 알고리즘 개념(prefix sum)
# 1차원 배열에서의 누적합 알고리즘
def get_sum(a, b):
    global psum
    return psum[b] - psum[a - 1]

N = 9

arr = [0, 1, 3, 10, -2, 3, -4, 10, 3, 8]
psum = [0] * (N+1)

# psum 갱신
for n in range(1, N + 1):
    psum[n] = psum[n - 1] + arr[n]

# 2부터 8까지의 합
print(get_sum(2, 8))


#2 차원 배열에서의 누적합 알고리즘
def get_sum(sy, sx, ey, ex):
    global psum
    return psum[ey][ex] - (psum[ey][sx - 1] + psum[sy - 1][ex] - psum[sy - 1][sx - 1])

N = 4
M = 5

arr = [
    [0, 0, 0, 0, 0, 0],
    [0, 10, 10, 3, 8, 4],
    [0, 9, 8, 4, 1, 10],
    [0, 7, 6, 5, 6, 5],
    [0, 2, 6, 6, 4, 10]
]

psum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# psum 갱신
for n in range(1, N + 1):
    for m in range(1, M + 1):
        psum[n][m] = (psum[n-1][m] + psum[n][m-1] - psum[n-1][m-1]) + arr[n][m]

# (3, 3)부터 (4, 5)까지의 2차원 합
print(get_sum(3, 3, 4, 5))





