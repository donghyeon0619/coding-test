# 트리 순회
# 실버 1
# 첫번째 풀이
# 트리 구현인데, 기존에 배울떄는 정수값이므로 리스트를 활용했는데,
# 문자를 저장할때는 리스트로 구성하면 인덱스값이 문자로 지정을 할수가 없어서
# key-value 형태에 dict를 사용해서 트리를 구성했음
N = int(input())
binary_tree = dict()

def pre_order(start_node):

    global binary_tree

    if start_node == '.':
        return

    print(start_node, end='')
    pre_order(binary_tree[start_node][0])
    pre_order(binary_tree[start_node][1])


def in_order(start_node):
    global binary_tree

    if start_node == '.':
        return

    in_order(binary_tree[start_node][0])
    print(start_node, end='')
    in_order(binary_tree[start_node][1])


def post_order(start_node):
    global binary_tree

    if start_node == '.':
        return

    post_order(binary_tree[start_node][0])
    post_order(binary_tree[start_node][1])
    print(start_node, end='')


for i in range(N):
    node, child_node1, child_node2 = input().split()
    binary_tree[node] = (child_node1, child_node2)


pre_order("A")
print()
in_order("A")
print()
post_order("A")

## 두번째 풀이
## 트리 구조를 dict 대신 배열을 사용해서 만든풀이
## 이때 ord()랑 chr를 통해서 문자를 아스키 코드로 변환하는 테크닉이 필요함
## "A"는 아스키 코드 65부터 시작
import sys
input = sys.stdin.readline

N = int(input())
tree = [[0, 0] for _ in range(N + 1)]


def pre_order(x):
    if x == 0:
        return
    print(chr(x + 64), end="")
    pre_order(tree[x][0])
    pre_order(tree[x][1])


def in_order(x):
    if x == 0:
        return
    in_order(tree[x][0])
    print(chr(x + 64), end="")
    in_order(tree[x][1])


def post_order(x):
    if x == 0:
        return
    post_order(tree[x][0])
    post_order(tree[x][1])
    print(chr(x + 64), end="")


for i in range(N):
    node, left, right = input().split()
    node = ord(node) - 64
    left = ord(left) - 64 if left != '.' else 0
    right = ord(right) - 64 if right != '.' else 0
    tree[node] = [left, right]

pre_order(1)
print()
in_order(1)
print()
post_order(1)
