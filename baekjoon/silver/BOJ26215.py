# 눈 치우기 문제
# 첫번째 풀이
# 리뷰
# 인덱스에 접근할 떄 해당 인덱스가 없을 수도 있는 엣지케이스도 생각할 수 있도록 해야함
# 예를들면 리스트가 하나인데 인덱스 0,1에 둘다 접근하면 인덱스 오류가 생기는 것 처럼 이것에 대해서도 조심해야함
import sys

readline = sys.stdin.readline

cnt = 0
N = int(readline())

cmd = list(map(int, readline().split()))

if len(cmd) > 1:
    while True:

        cmd = sorted(cmd, reverse=True)
        if cmd[0] < 0:
            break
        elif cmd[1] > 0:
            cmd[0] -= 1
            cmd[1] -= 1
            cnt += 1
        else:
            cnt += cmd[0]
            break
else:
    cnt += cmd[0]

print(-1 if cnt > 1440 else cnt)


# 두번째 풀이
# 이 풀이는 max를 이용해서 푼 문제 정렬하고 다시 루프를하게되면 m * n log n 이 걸리게되면 비효율적임, max를 구해서 하는것이 가장 적절

a=input()
a=list(map(int,input().split()))
b=max(sum(a)//2+sum(a)%2,max(a))
print(-1 if b>1440 else b)

# 세번쨰 풀이
# 이것도 비슷한 풀이
n = int(input())
a = list(map(int, input().split()))
ans = max((sum(a)+1)//2, max(a))
print(-1 if ans > 1440 else ans)


# 네번째 풀이
# 힙을 이용하면서 최대힙을 이용한 방식
# 'PriorityQueue' 라이브러리를 사용하는 방법도 있고, heapq를 이용하는 방식이 있는데 코딩테스트에서는 heapq를 이용하는 방식이 적절함

import heapq
import sys

N = int(sys.stdin.readline())
snow = list(map(int, sys.stdin.readline()))

heap = [-x for x in snow if x > 0]
heapq.heapify(heap)

minutes = 0
while heap:
    # 1번 큰 집 꺼내기
    a = -heapq.heappop(heap)

    # 두 번쨰 집이 있으면 같이 처리
    if heap:
        b = -heapq.heappop(heap)
        a -= 1
        b -= 1
        minutes += 1
        if a > 0:
            heapq.heappush(heap, -a)
        if b > 0:
            heapq.heappush(heap, -b)
    else:
        # 마지막 집만 남았으면 한 분에 1씩
        minutes += a
        break

print(-1 if minutes > 1440 else minutes)


