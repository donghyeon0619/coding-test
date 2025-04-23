import sys

N = int(sys.stdin.readline())
queue = []


for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if "push" in cmd:
        queue.append(cmd.split()[1])
    elif "pop" == cmd:
        print(queue.pop(0) if queue else -1)
    elif "size" == cmd:
        print(len(queue))
    elif "empty" == cmd:
        print(0 if queue else 1)
    elif "front" == cmd:
        print(queue[0] if queue else -1)
    elif "back" == cmd:
        print(queue[-1] if queue else -1)




