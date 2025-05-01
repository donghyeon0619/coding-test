# 크로아티아 알파벳 문제
# 첫번쨰 풀이
# 리뷰
# len(리스트) 같은 자주 쓰는 문자들은 다시 쓸 수 있으니 미리 참조 객체를 선언하는것이 비용이 적게 들지
cmd = input()
cnt = 0
i = 0
length = len(cmd)

while i < length:
    cnt += 1
    if cmd[i:i+3] == 'dz=':
        if i + 3 == length:
            break
        else:
            i += 3

    elif cmd[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        if i + 2 == length:
            break
        else:
            i += 2
    else:
        i += 1


print(cnt)


# 두번쨰 풀이
# 미리 lis를 정의 해놓고 처음 내 풀이에서 if문 내부의 if문을 바깥의 조건식으로 뺸 것이고, 로직은 결국에 똑같다.

x = input()

listA = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']  # dz제외
listB = ['dz=']
cnt = 0
i = 0

# while을써서 i를 수동으로 조정
while i < len(x):  # 5자리면 4가 마지막 index
    if x[i:i + 2] in listA and i + 1 < len(x):  # 범위초과 방지
        cnt += 1
        i += 2
    elif x[i:i + 3] in listB and i + 2 < len(x):
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1

print(cnt)

# 세번째 풀이
# "한 글자로 취급한다고 했었으므로" 치환을 해도 상관이 없음.
# 목록에 있는 해당 문자열이 있으면 그 글자를 하나의 문자열로 치환하고 풀이 해도됨
# 문자열의 replace함수는 c레벨에서 동작해서 성능도 빠른 편이고 문자열의 슬라이싱과 비교해보다도
# replace의 시간복잡도는 훨씬 작은 편

cro = ["c=", 'c-', "dz=", "d-", "lj", "nj", "s=", "z="]

a = input()

for i in cro:
    a = a.replace(i, "*")
print(len(a))
