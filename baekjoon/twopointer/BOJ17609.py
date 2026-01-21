# 회문 (골드 5)
# 첫번쨰 풀이
# for문 안에서 단순히 elif를 쓰지 않고 if문을 나열할때, 해당 if문이 전부 실행될 수 있으므로
# break나 continue와 같은 분기문을 알차게 써야함
# 유사회문에서 지우면 회문이 나온다는 것을 알 수 있는데 이것을 역으로 생각했을떄
# 회문에서 하나 추가하면 "유사회문"이 나온다는 것을 인지할 수 있음
T = int(input())
ans = [0] * T


def is_pal(left, right, char):
    while left < right:
        if char[left] != char[right]:
            return False

        left += 1
        right -= 1

    return True


for i in range(T):
    char = list(input())
    left = 0
    right = len(char) - 1
    while left < right:
        if char[left] == char[right]:
            left += 1
            right -= 1
            continue

        if is_pal(left + 1, right, char) or is_pal(left, right - 1, char):
            ans[i] = 1
            break
        else:
            ans[i] = 2
            break


for t in range(T):
    print(ans[t])


# 두번째 풀이
# 여기서 문제에서 회문인지 유사회문인지 구하는 것인데
# 이때 각각 회문인지 유사회문인지 각각 구하게 되면 O(N) + O(N)이 되므로 결국엔 O(N)이 되게 됨
# 그리고 다른지점이 나오면 그 지점을 무조건 지워야 이득이라는 것을 알 수 있는데 이는 "그리디"적 사고라고 볼 수 있음
# 이 풀이는 첫번째 풀이랑 사고는 비슷하지만
# 슬라이싱을 통해서 문자열 복사가 발생하게 되므로 이때 발생하는 비용이 문제가 되고
# 그리고 절반만 탐색하면 되는데 for문을 통해서 전체를 탐색하므로 시간이 더 걸리게됨
# 코드적으로는 깔끔해 보이지만 시간복잡도는 두배차이가 나는 단점이 있음
def is_palindrome(s):
    for left in range(len(s)):
        right = len(s) - left - 1
        if s[left] != s[right]:
            return False

    return True


def is_pseudo_palindrome(s):
    for left in range(len(s)):
        right = len(s) - left - 1
        if s[left] != s[right]:
            s1 = s[:left] + s[left + 1:]
            s2 = s[:right] + s[right+1:]
            if is_palindrome(s1) or is_palindrome(s2):
                return True
            else:
                return False


def solve():

    s = input()
    if is_palindrome(s):
        print(0)
        return

    if is_pseudo_palindrome(s):
        print(1)
        return

    print(2)


T = int(input())
for _ in range(T):
    solve()
