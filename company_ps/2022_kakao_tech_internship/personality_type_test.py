"""
    제목: 성격 유형 검사하기
    난이도: Essential

"""
# 첫번째 풀이(내 풀이)

def solution(survey, choices):
    type_num = {1: ("R", "T"), 2: ("C", "F"), 3: ("J", "M"), 4: ("A", "N")}
    kakao_type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    answer = ''

    for i in range(len(survey)):
        if choices[i] > 4:
            kakao_type[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            kakao_type[survey[i][0]] += 4 - choices[i]

    for i in range(1, 5):
        a, b = type_num[i][0], type_num[i][1]
        if kakao_type[a] > kakao_type[b]:
            answer += a
        elif kakao_type[a] < kakao_type[b]:
            answer += b
        elif a < b:
            answer += a
        else:
            answer += b

    return answer

# 두번째 풀이(내 풀이에서 리펙토링한 풀이)
def solution(survey, choices):
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N",)]
    kakao_type = {ch: 0 for ch in "RTCFJMAN"}

    answer = ""

    for s, choice in zip(survey, choices):
        if choice > 4:
            kakao_type[s[1]] += choice - 4
        elif choice < 4:
            kakao_type[s[0]] += 4 - choice

    for a, b in pairs:
        if kakao_type[a] >= kakao_type[b]:
            answer += a
        else:
            answer += b

    return answer

# 세번째 풀이
# 위에 풀이랑 똑같지만, types 단순히 배열에다가 저장함
types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']

def solution(survey, choices):
    score = {t: 0 for t in types} # scores[t]: 성격 유형 t의 점수

    # 점수 계산
    for s, c in zip(survey, choices):
        if c <= 3:
            score[s[0]] += (4 - c)
        elif c >= 5:
            score[s[1]] += (c - 4)

    # 답 구하기
    ans = ""
    for i in range(4):
        s1, s2 = score[types[2 * i]], score[types[2 * i + 1]]
        if s1 >= s2:
            ans += types[2 * i]
        else:
            ans += types[2 * i + 1]

    return ans