# 신고 결과 받기
# 첫번째 풀이 (내 풀이)
# 변수명등에서 헷갈리지 않도록 조심성있게 선언하자

def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n

    mapper = dict()
    report_m = dict()

    for i in range(n):
        report_m[id_list[i]] = []
        mapper[id_list[i]] = i

    for i in range(len(report)):
        x, y = report[i].split()
        if x not in report_m[y]:
            report_m[y].append(x)

    for j in range(n):
        name = id_list[j]
        cnt = len(report_m[name])
        if cnt < k:
            continue

        for m in range(cnt):
            answer[mapper[report_m[name][m]]] += 1

    return answer

## 두번째 풀이
## list를 통해서 도는것 보단 set 자료구조를 이용해서 도는 것이 중요
## 작명도 반영된 것
## 그리고 초기 세팅값에 편리한 defaultdict를 사용
from collections import defaultdict

def solution(id_list, report, k):
    n = len(id_list)
    answer = [0] * n

    id_to_idx = {user_id: i for i, user_id in enumerate(id_list)}
    reported_by = defaultdict(set)

    # 중복 신고 제거 + 수집
    for r in report:
        reporter, reported = r.split()
        reported_by[reported].add(reporter)

    # 정지 대상 처리
    for reporters in reported_by.values():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[id_to_idx[reporter]] += 1

    return answer


## 세번째 풀이(강의 풀이)
## 이 풀이는 내가 푼 풀이랑 다르게 신고자 관점에서 풀이임
def solution(id_list, report, k):
    st = set()
    for r in report:
        a, b = r.split()
        st.add((a, b))

    count = {name: 0 for name in id_list}
    report_set = {name: set() for name in id_list}

    for name1, name2 in st:
        report_set[name1].add(name2)
        count[name2] += 1

    ans = []
    for name in id_list:
        cnt = 0
        for n in report_set[name]:
            cnt += (count[n] >= k)
        ans.append(cnt)

    return ans
