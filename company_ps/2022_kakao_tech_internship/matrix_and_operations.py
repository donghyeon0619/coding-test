"""
Programmers - 행렬과 연산자
난이도: Advanced
분류: 자료구조 (deque), 시뮬레이션

Author: donghyeon
Date: 2026-05-21

[문제 요약]
- r행 c열 행렬에 두 가지 연산을 순서대로 적용한 최종 상태를 반환
  1) ShiftRow: 모든 행이 아래로 한 칸씩 이동 (마지막 행 → 첫 행)
  2) Rotate:   행렬의 바깥 테두리를 시계 방향으로 한 칸 회전 (안쪽은 그대로)
- 제약: r * c ≤ 100,000, operations 길이 ≤ 100,000

[핵심 관찰]
- 단순 시뮬레이션은 O(operations × r × c) = 최대 10^10 → 시간 초과
- 두 연산의 본질:
    * ShiftRow는 셀의 "값"을 옮기는 게 아니라 "어느 행이 위인지"만 바뀜
    * Rotate는 테두리(2r + 2c - 4 셀)만 건드리고 안쪽은 손 안 댐
- 행렬을 적절한 조각으로 나누고, 각 조각을 deque로 관리하면 두 연산 모두 O(1)에 처리 가능
- 핵심 트릭: deque의 appendleft + pop (또는 append + popleft)은
  "한 칸 밀기 + 끝에서 빼내기"를 O(1)에 동시에 처리해줌

[풀이 비교]
- 풀이 1 (6분할): 4코너 + 4변 내부 + inner 영역으로 세밀하게 분해
    → 각 부분의 역할이 명확하지만 코드량이 많고 분기가 늘어남
- 풀이 2 (3분할): left_pillar, mid_pillar, right_pillar 세 세로 기둥으로 분해
    → ShiftRow가 세 기둥의 rotate(1) 3번으로 끝나는 가장 깔끔한 형태
    → 일반적인 모범 풀이

[시간 복잡도]
- 초기화: O(r × c)
- 각 연산: O(1)
- 최종 결과 조립: O(r × c)
- 총합: O(r × c + operations)  → 최대 약 2 × 10^5, 매우 여유로움

[공간 복잡도]
- O(r × c) — 행렬 데이터를 deque 형태로 보관

[복습 포인트]
- 정확성/효율성 두 가지 점수가 분리된 문제 유형:
  효율성 풀이가 안 떠오르면 일단 정확성 풀이라도 작성해서 부분 점수 확보할 것
- deque 메서드 활용이 핵심:
    * appendleft / append / popleft / pop  →  모두 O(1)
    * rotate(k)  →  k가 작으면 O(k), 보통 rotate(1)/rotate(-1)로 사용
- "appendleft(x) + pop()" 패턴: 한 칸 오른쪽으로 밀고 끝값 추출 (Rotate의 핵심 트릭)
- ShiftRow처럼 "전체가 한 칸 이동"하는 연산은 데이터 복사가 아니라
  외부 컨테이너의 rotate(1) 한 줄로 끝낼 수 있다는 사고방식이 중요
"""


# ============================================================================
# 풀이 1 — 6분할 (내 풀이)
# ----------------------------------------------------------------------------
# [접근 아이디어]
# 처음 사고 흐름은 일리 있었지만, 구역을 쪼개서 deque로 관리해야 한다는 핵심을
# 스스로 떠올리지 못했음. AI 힌트를 받고 다음 6조각으로 행렬을 분해:
#   - 코너 4개 (tl, tr, bl, br): 스칼라
#   - top_inner, bottom_inner:   각 변의 안쪽 (deque, 길이 c-2)
#   - left_inner, right_inner:   각 변의 안쪽 (deque, 길이 r-2)
#   - inner:                     안쪽 행렬 (deque of deque)
#
# [핵심]
# 모든 조각을 deque로 두어 두 연산을 O(1)에 처리.
# Rotate는 4개 변에 대해 "appendleft + pop" / "append + popleft" 패턴 사용.
# ShiftRow는 inner를 rotate(1)로 통째 회전 + 변/코너 값들을 참조 교체.
# ============================================================================
from collections import deque


def solution(rc, operations):
    row = len(rc)
    col = len(rc[0])

    # --- 초기화: 행렬을 6조각으로 분해 ---
    tl = rc[0][0]
    tr = rc[0][-1]
    bl = rc[row - 1][0]
    br = rc[row - 1][-1]

    top_inner = deque(rc[0][1:-1])
    bottom_inner = deque(rc[row - 1][1:-1])
    left_inner = deque(rows[0] for rows in rc[1:-1])
    right_inner = deque(rows[-1] for rows in rc[1:-1])

    inner = deque()
    for i in range(1, row - 1):
        inner.append(deque(rc[i][1:-1]))

    # --- 연산 처리 ---
    for operation in operations:
        if operation == 'Rotate':
            # 각 변에 대해 "이전 코너를 끼우고 끝값을 다음 코너로 빼내기"
            top_inner.appendleft(tl)
            nxt_tr = top_inner.pop()

            right_inner.appendleft(tr)
            nxt_br = right_inner.pop()

            bottom_inner.append(br)
            nxt_bl = bottom_inner.popleft()

            left_inner.append(bl)
            nxt_tl = left_inner.popleft()

            tl, tr, br, bl = nxt_tl, nxt_tr, nxt_br, nxt_bl

        else:  # ShiftRow: 모든 행이 한 칸 아래로
            # 왼쪽 기둥: tl을 위로 넣고 bl로 흘려보냄
            left_inner.appendleft(tl)
            nxt_bl = left_inner.pop()
            tl, bl = bl, nxt_bl

            # inner: top_inner를 맨 위에 끼우고 bottom_inner를 새로 받음
            inner.appendleft(top_inner)
            nxt_bi = inner.pop()
            top_inner = bottom_inner
            bottom_inner = nxt_bi

            # 오른쪽 기둥: tr을 위로 넣고 br로 흘려보냄
            right_inner.appendleft(tr)
            nxt_br = right_inner.pop()
            tr, br = br, nxt_br

    # --- 결과 조립 ---
    top = [tl] + list(top_inner) + [tr]
    middle = [
        [left_inner[i]] + list(inner[i]) + [right_inner[i]]
        for i in range(row - 2)
    ]
    bottom = [bl] + list(bottom_inner) + [br]

    return [top] + middle + [bottom]


# ============================================================================
# 풀이 2 — 3분할 (모범 풀이)
# ----------------------------------------------------------------------------
# [접근 아이디어]
# 행렬을 세 개의 세로 기둥으로만 쪼갬:
#   - left_pillar:  첫 번째 열 전체 (코너 포함)
#   - mid_pillar:   가운데 열들 (각 행의 안쪽; deque of deque)
#   - right_pillar: 마지막 열 전체 (코너 포함)
#
# [핵심]
# - ShiftRow가 세 기둥의 rotate(1) 세 번으로 끝남 → 매우 깔끔
# - Rotate에서는 (0,0)→(0,1)→...→(0,c-1)→(1,c-1)... 회전을
#   네 번의 pop/append 호출로 처리
# - col == 2일 때 mid_pillar의 각 행이 빈 deque가 되므로 분기 처리
#
# 강의에서도 동일한 방식으로 풀이됨. 다음에 비슷한 문제 만나면
# "세로 기둥 분해 + 외부 rotate" 패턴을 먼저 떠올릴 것.
# ============================================================================
from collections import deque


def solution(rc, operations):
    answer = []

    # --- 초기화: 세 기둥으로 분해 ---
    mid_pillar, left_pillar, right_pillar = deque(), deque(), deque()
    for r in rc:
        mid_pillar.append(deque(r[1:-1]))
        left_pillar.append(r[0])
        right_pillar.append(r[-1])
    # [같은 초기화 — comprehension 버전]
    # left_pillar  = deque(r[0]  for r in rc)
    # right_pillar = deque(r[-1] for r in rc)
    # mid_pillar   = deque(deque(r[1:-1]) for r in rc)

    # --- 연산 처리 ---
    for operation in operations:
        if operation == 'Rotate':
            if mid_pillar[0]:
                # 일반 케이스: 가운데 열이 존재할 때
                #   (0,c-2) → (0,c-1):     mid_pillar[0].pop() → right_pillar 앞
                #   (r-1,c-1) → (r-1,c-2): right_pillar.pop()  → mid_pillar[-1] 끝
                #   (r-1,1) → (r-1,0):     mid_pillar[-1].popleft() → left_pillar 끝
                #   (0,0) → (0,1):         left_pillar.popleft() → mid_pillar[0] 앞
                right_pillar.appendleft(mid_pillar[0].pop())
                mid_pillar[-1].append(right_pillar.pop())
                left_pillar.append(mid_pillar[-1].popleft())
                mid_pillar[0].appendleft(left_pillar.popleft())
            else:
                # 엣지 케이스: col == 2 → mid_pillar의 행이 비어있음
                # 좌우 기둥끼리만 코너 값 교환
                right_pillar.appendleft(left_pillar.popleft())
                left_pillar.append(right_pillar.pop())
        else:
            # ShiftRow: 세 기둥을 모두 한 칸 아래로 회전
            mid_pillar.rotate(1)
            left_pillar.rotate(1)
            right_pillar.rotate(1)

    # --- 결과 조립 ---
    for left, mid, right in zip(left_pillar, mid_pillar, right_pillar):
        answer.append([left] + list(mid) + [right])

    return answer
    # [같은 리턴 — list comprehension 버전]
    # return [
    #     [left_pillar[i]] + list(mid_pillar[i]) + [right_pillar[i]]
    #     for i in range(len(rc))
    # ]