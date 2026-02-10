# 이진 트리란?
# - 루트 노드가 존재하는 루트 트리이다
# - 최대 2개의 자식 노드 까지만 가질 수 있다
#
# 이진 트리의 순회 방법
# - 참고
#   : 일반적인 트리의 순회는 그래프 순회에서 사용되는 "DFS"나 "BFS"를 이용해서 구현하면 됨
#
# 1. 전위 순회
#   - 특징
#       : 부모노드 -> 왼쪽 자식 노드 -> 오른쪽 자식 노드
#   - 코드
N = 10
root_node = 5

def pre_order(node):
    global tree

    # base case
    if node == None:
        return

    # recursive case
    print(node, end=' ')
    pre_order(tree[node][0])
    pre_order(tree[node][1])


tree = [[None, None] for _ in range(N + 1)]

tree[1] = [10, None]
tree[2] = [None, None]
tree[3] = [None, None]
tree[4] = [3, 9]
tree[5] = [1, 4]
tree[6] = [None, None]
tree[7] = [None, None]
tree[8] = [None, None]
tree[9] = [2, 6]
tree[10] = [8, 7]

pre_order(5)

# 2. 중위 순회
#   - 특징
#       : 왼쪽 자식 노드 -> 부모 노드 -> 오른쪽 자식 노드
#   - 코드
N = 10
root_node = 5

def in_order(node):
    global tree

    # base case
    if node == None:
        return

    # recursive case
    in_order(tree[node][0])
    print(node, end=' ')
    in_order(tree[node][1])


tree = [[None, None] for _ in range(N + 1)]

tree[1] = [10, None]
tree[2] = [None, None]
tree[3] = [None, None]
tree[4] = [3, 9]
tree[5] = [1, 4]
tree[6] = [None, None]
tree[7] = [None, None]
tree[8] = [None, None]
tree[9] = [2, 6]
tree[10] = [8, 7]

in_order(5)

# 3. 후위 순회
#   - 특징
#       : 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 부모 노드
#   - 코드
N = 10
root_node = 5

def post_order(node):
    global tree

    # base case
    if node == None:
        return

    # recursive case
    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end=' ')


tree = [[None, None] for _ in range(N + 1)]

tree[1] = [10, None]
tree[2] = [None, None]
tree[3] = [None, None]
tree[4] = [3, 9]
tree[5] = [1, 4]
tree[6] = [None, None]
tree[7] = [None, None]
tree[8] = [None, None]
tree[9] = [2, 6]
tree[10] = [8, 7]

post_order(5)
