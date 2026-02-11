# 첫번째 풀이
# 직관적이긴 하나 코드가 너무 김
# 파이썬스럽게 풀지 못했음.
# 이 문제는 그리한 사고를 하여 해결하면 됨
def solution(lottos, win_nums):
    answer = []

    unknown_nums = 0
    correct_nums = 0

    for i in range(6):
        for j in range(6):
            if lottos[i] == 0:
                unknown_nums += 1
                break

            elif lottos[i] == win_nums[j]:
                correct_nums += 1
                break

    best = correct_nums + unknown_nums
    worst = correct_nums

    if best == 6:
        answer.append(1)
    elif best == 5:
        answer.append(2)
    elif best == 4:
        answer.append(3)
    elif best == 3:
        answer.append(4)
    elif best == 2:
        answer.append(5)
    else:
        answer.append(6)

    if worst == 6:
        answer.append(1)
    elif worst == 5:
        answer.append(2)
    elif worst == 4:
        answer.append(3)
    elif worst == 3:
        answer.append(4)
    elif worst == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer

## 두번째 풀이(다른사람 풀이)
## rank라는 변수를 두고, 그리고 count()함수를 사용해서
## 간략하게 풀이함
def solution(lottos, win_nums):
        rank = [6, 6, 5, 4, 3, 2, 1]

        cnt_0 = lottos.count(0)
        ans = 0
        for x in win_nums:
            if x in lottos:
                ans += 1

        return rank[cnt_0 + ans], rank[ans]

## 세번째 풀이(다른 사람 풀이)
## set이랑 dict를 이용한 풀이
## 그리고 set(집합)으로 만들어서 교집합, 합집합을 이용해서 이용한 풀이
## 자주 생각해볼만 사고방식인 것 같음
## 좀더 파이썬 스러운 풀이
##
def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1,
    }

    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]


