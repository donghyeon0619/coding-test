## 그룹 단어 체커 문제
## 첫번째 풀이
## 루프당 len(ㅎ)도 함수 호출이므로 불필요한 함수 호출은 자제 하는 것이 좋음
## 그리고 가능하면 파이썬 내장 함수 (c레벨)에서  구현된 것을 적극 사용하는 것이 좋음
## 그리고 내장함수라도 insert(), del, remove 같은 함수들은 비용이 크므로 자제하는 것이 좋음
import sys

readline = sys.stdin.readline

N = int(readline())
group_num = 0

for _ in range(N):
    cmd = readline()
    temp = []
    if len(cmd) == 1:
        group_num += 1
    else:
        for i in range(len(cmd)):
            if i == 0:
                temp.append(cmd[i])
            if i > 0 and cmd[i] != cmd[i-1]:
                if cmd[i] in temp:
                    break
                if i == len(cmd) - 1:
                    group_num += 1
                    break
                temp.append(cmd[i])

print(group_num)

## 두번째 풀이
## 그룹 단어 문제의 범위가 N <= 100 이고, 각 문자열 길이도 비교적 작으므로, input을 사용해도 속도차이 무시 가능
## 정렬을 이용해서 정렬이 만약 이뤄지게 된다면, 문자간의 연속되지 않은 구역이 있었다는 소리이므로 이를 이용해도 됨
## sorted()는 C로 최적화된 timeSort를 사용해 O(n log n)으로 동작하고,
## 키 값은 한번만 계산해두고 재사용함으로 파이썬 레벨에서 for-in 루프와 in 검사를 직접 여러번 도는 것보다 빠름
N = int(input())
count = 0

for _ in range(N):
  cmd = input()
  if list(cmd) == sorted(cmd, key=cmd.find):
    count += 1

print(count)

## 세번쨰 풀이
## 받은 문자열 개수에서 차감을 시키는 방법,
## 이 코드에서는 차감을 하는 것이므로 문자열의 길이가 1일때는 생각을 안해줘도 됨.
## 그리고 input은 개행문자를 포함하지 않고 반환함.

n = int(input())
con = n
for i in range(n):
  a = input()
  for j in range (0,len(a)-1):
    if a[j] == a[j+1]:
      pass
    elif a[j] in a[j+1:]:
      con -= 1
      break
print(con)


## 4번쨰 풀이
## 파이썬에서만 쓰이는 for_else가 구조가 쓰이고 내가 처음에 푼 풀이랑 비슷한 풀이
## for_else는 for문에서 break문을 만나지 않으면 else문이 실행되고 만약 break문을 만나면 else문이 실행되지 않음
n = int(input())
l = []
sum = 0
for i in range(n):
    a = input()
    l = []
    for i in range(len(a)):
        if a[i] in l:
            if l[i-1] != a[i]:
                break
        l.append(a[i])
    else:
        sum+=1
print(sum)




