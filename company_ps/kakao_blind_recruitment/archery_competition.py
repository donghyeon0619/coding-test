# 양궁대회 (다시 풀어볼 문제)
# 구현하지 못함
# 문제가 간단해보이지만 어려움
# 첫번째 풀이(강의 풀이)
# 브루트 포스적인 풀이로 문제를 해결
# 중복조합을 이용했음O(11Hn)
# 파이썬의 combinations_with_replacement 함수를 이용
from itertools import combinations_with_replacement


def get_cur_point(apeach, lion):
    apeach_point = 0
    lion_point = 0

    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        if apeach[i] >= lion[i]:
            apeach_point += 10 - i
        else:
            lion_point += 10 - i

    return lion_point - apeach_point


def solution(n, info):
    best_point = 0
    best_result = [0] * 11

    for comb in combinations_with_replacement(range(11), n):
        cur_result = [0] * 11

        for num in comb:
            cur_result[num] += 1

        cur_point = get_cur_point(info, cur_result)
        if (cur_point > best_point) or (cur_point == best_point and cur_result[::-1] > best_result[::-1]):
            best_point = cur_point
            best_result = cur_result[:] # shallowcopy

    return [-1] if best_point == 0 else best_result

## 두번째 풀이(다른사람 풀이)
## dp를 이용한 풀이
def solution(n, info_A):
    info_L = [0]*11
    arrow_L = [i+1 for i in info_A[:-1]]
    rate = [[10-index,(2-(hit==1))*(10-index),hit] for index,hit in enumerate(arrow_L)]
    rate.sort(key=lambda x:x[0])
    dp = [[0,[],11] for _ in range(n+1)]
    for a,b,c in rate:
        for x in range(n,c-1,-1):
            if dp[x-c][0]+b > dp[x][0] or (dp[x-c][0]+b == dp[x][0] and dp[x-c][2] < dp[x][2]):
                dp[x][0] = dp[x-c][0]+b
                dp[x][1] = dp[x-c][1]+[a]
                dp[x][2] = min(dp[x][1])
    for i in dp[n][1]:
        info_L[10-i] = arrow_L[10-i]
    info_L[-1] = n-sum(info_L)
    answer = sum(((l>a)-(a>l))*(10-index) for index,(a,l) in enumerate(zip(info_A,info_L)))
    return info_L if answer>0 else [-1]

# ## 세번째 풀이(다른사람 풀이)
## product를 이용한 풀이
from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    maxd = 0
    for wl in product((True, False), repeat=11):
        t = 0
        s = sum(info[i]+1 for i in range(11) if wl[i])
        if s <= n:
            apeach = sum(i for i in range(11) if not wl[i] and info[i])
            ryan = sum(i for i in range(11) if wl[i])
            d = ryan-apeach
            if d > maxd:
                maxd = d
                ans = [info[i]+1 if wl[i] else 0 for i in range(11)]
                ans[0] += n-s
    ans.reverse()
    return ans

# ## 4번째풀이(다른사람 풀이)
# dfs로 푼 풀이
def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]