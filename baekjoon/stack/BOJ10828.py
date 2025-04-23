## 스택 문제
## 한 두줄 입력 받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야할 때는 input()으로 입력을 받게 된다면 시간초과 발생할 수 있음
## 코테는 입력때마다 출력을 해도 상관이 없음
## 첫번째 풀이
def print_data(arr):
    for j in arr:
        print(j)


num = int(input())
s = []
oup = []

for _ in range(num):
    inp = input().split()
    cmd = inp[0]

    if cmd == 'push':
        s.append(int(inp[1]))
    elif cmd == 'pop':
        if not s:
            oup.append('-1')
        else:
            oup.append(s.pop())
    elif cmd == 'size':
        oup.append(len(s))
    elif cmd == 'empty':
        oup.append(0 if s else 1)
    elif cmd == 'top':
        if not s:
            oup.append('-1')
        else:
            oup.append(s[-1])

print_data(oup)



## 두번쨰 풀이
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().strip()

    if "push" in cmd:
        stack.append(cmd.split()[1])
    elif cmd == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if stack else 1)
    elif cmd == 'top':
        print(stack[-1]) if stack else print(-1)



