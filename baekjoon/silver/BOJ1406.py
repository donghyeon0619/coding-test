## 에디터 문제
## 첫번쨰 풀이
## 리뷰
## 시간 초과 발생 -> insert 및 del은 요소를 삽입 및 삭제 이후 요소를 전부 한칸씩 뒤로 밀거나 앞으로 밀게 되므로 O(n)이 걸리게 됨.
## 그러므로 최악의 경우 N번의 삽입/삭제에 대해 매번 n만큼 이동이 일어나서 O(n*N)이 되어버리게 됨
## 알고리즘에서는 자제하는 것이 좋음
# import sys
#
#
# inp = list(sys.stdin.readline().strip())
# N = int(sys.stdin.readline())
# cursor = len(inp)
#
# for _ in range(N):
#     cmd = sys.stdin.readline().strip()
#     if 'P' in cmd:
#         inp.insert(cursor, cmd.split()[1])
#         cursor += 1
#     elif 'L' == cmd:
#         if cursor > 0:
#             cursor -= 1
#     elif 'D' == cmd:
#         if cursor < len(inp):
#             cursor += 1
#     elif 'B' == cmd:
#         if cursor > 0:
#             del inp[cursor - 1]
#             cursor -= 1
#
#
# print(''.join(inp))


## 두번째 풀이 (이중스택을 이용)
## 리뷰
## 시간초과 없이 맞췄지만 228ms나 걸렸음, for문마다 strip() 실행하는 것과, split()하는 것에서 오버헤드가 발생.
# import sys
#
# left = list(sys.stdin.readline().strip())
# right = []
# N = int(sys.stdin.readline())
#
# for _ in range(N):
#     cmd = sys.stdin.readline().strip()
#     if 'P' in cmd:
#         left.append(cmd.split()[1])
#     elif 'L' == cmd:
#         if left:
#             right.append(left.pop())
#     elif 'D' == cmd:
#         if right:
#             left.append(right.pop())
#     elif 'B' == cmd:
#         if left:
#             left.pop()
#
# print(''.join(left) + ''.join(reversed(right)))


## 세번째 풀이(이중스택을 이용하며, 연산최소화)
import sys

readline = sys.stdin.readline

left = list(readline().strip())
right = []
N = int(readline())

lappend = left.append
rappend = right.append
lpop = left.pop
rpop = right.pop


for _ in range(N):
    cmd = readline()
    if cmd[0] == 'P':
        lappend(cmd[2])
    elif cmd[0] == 'L':
        if left:
            rappend(lpop())
    elif cmd[0] == 'D':
        if right:
            lappend(rpop())
    elif cmd[0] == 'B':
        if left:
            lpop()

print(''.join(left) + ''.join(right[::-1]))


