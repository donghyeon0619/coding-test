"""
[다단계 칫솔 판매]

✔ 문제 핵심
- 추천 관계는 '부모가 1명인 트리 구조'
- 판매 금액은 10%씩 위(추천인)로 전달
- 10% 계산 시 원 단위 절사
- 전달 금액이 1원 미만이면 전파 종료

✔ 구현 전략
- 이름 → 추천인 관계를 dict로 저장 (부모 포인터 개념)
- 판매 발생 시 재귀/반복을 통해 부모 방향으로 상향 전파
- 각 단계마다:
    전달금 = price // 10
    본인수익 = price - 전달금
    전달금이 0이면 종료

✔ 주의사항
- 판매를 미리 합치면 안 됨 (정수 절사 때문에 결과 달라질 수 있음)
- 실수 연산(price * 0.1) 대신 정수 나눗셈(price // 10) 권장
- 반복문 방식이 재귀보다 약간 더 빠름

✔ 시간 복잡도
- 판매 건수 M (≤100,000)
- 각 전파 깊이 ≈ log10(price) ≈ 최대 7~8
- 전체 시간복잡도 ≈ O(M)
"""
# 첫번째 풀이(내 풀이)
# 처음에 시간초과가 난 풀이
def solution(enroll, referral, seller, amount):
    answer = [0] * (len(enroll))

    for i in range(len(seller)):
        sr, am = seller[i], amount[i]
        price = 100 * am
        start = find_idx(sr, enroll)

        while start >= 0:
            if (price // 10) < 1:
                answer[start] += price
                break

            answer[start] += price - (price // 10)

            if referral[start] == '-':
                break

            for j in range(start, -1, -1):
                if referral[start] == enroll[j]:
                    start = j
                    price //= 10
                    break

    return answer


def find_idx(x, arr):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

# 두번째풀이
# dict과 같은 hashmap구조에 자료구조를 사용함
# 이런 문제는 hash와 부모 포인터 배열 핵심
# 그리고 이 문제는 주의할 것이 중복된 sellor가 나온다고 해서
# 최적화하기 위해 합쳐서 하면 안됨, 합치게 되면
# 수학적 정합성이 깨질 수 있음
def solution(enroll, referral, seller, amount):
    ans = [0] * (len(enroll))
    n = len(enroll)
    idx = {name: i for i, name in enumerate(enroll)}
    parent = [-1] * n
    for i in range(n):
        if referral[i] != '-':
            parent[i] = idx[referral[i]]

    for sr, am in zip(seller, amount):
        start = idx[sr]
        price = am * 100

        while start != -1 and price > 0:
            pass_up = price // 10
            keep = price - pass_up
            ans[start] += keep

            if pass_up < 1:
                break

            start = parent[start]
            price = pass_up

    return ans

# 세번째풀이
# 위에 풀이랑 비슷하지만 하나의 함수로 빼내서 풀었고
# money라는 수익을 저장하는 dict변수를 선언
def query(name, price):
    global money, tree

    price10 = int(price * 0.1)
    money[name] += price - price10

    if price10 == 0:
        return

    if name != '-':
        query(tree[name], price10)


def solution(enroll, referral, seller, amount):
    global money, tree

    money = dict()
    money['-'] = 0
    for name in enroll:
        money[name] = 0

    tree = dict()
    for child, parent in zip(enroll, referral):
        tree[child] = parent

    for name, num in zip(seller, amount):
        query(name, num * 100)

    ans = [money[name] for name in enroll]

    return ans

