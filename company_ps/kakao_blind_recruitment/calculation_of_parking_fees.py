# ## 주차 요금 계산
# ## 난이도 essential
# ## 첫번째 풀이
# ## 해당 문제에 대해서 시간을 총분으로 바꿀 때 사용하는 컨트롤이랑
# ## 딕셔너리 초기 세팅, 그리고,
# ## 정수 올림수 구하는 로직에 대해서 구하는 방법에 대해서 생각해봄
from collections import defaultdict

END_TIME = (23 * 60) + 59

def solution(fees, records):

    answer = []

    basic_time, basic_fee, per_minutes, per_fees = fees[0], fees[1], fees[2], fees[3]
    cars_records = defaultdict(list)
    cars_total_times = defaultdict(int)
    cars_total_money = defaultdict(int)
    for record in records:
        times, car_nums, comment = record.split()
        car_nums = int(car_nums)
        h, m = map(int, times.split(":"))
        minutes = h * 60 + m
        cars_records[car_nums].append(minutes)

    for car_num, times in cars_records.items():
        n = len(times)
        if n % 2 == 1:
            for i in range(0, n-1, 2):
                cars_total_times[car_num] += times[i + 1] - times[i]
            cars_total_times[car_num] += END_TIME - times[-1]
        else:
            for i in range(0, n, 2):
                cars_total_times[car_num] += times[i + 1] - times[i]

    for car_num, times in cars_total_times.items():
        if times <= basic_time:
            cars_total_money[car_num] += basic_fee
        else:
            cars_total_money[car_num] += basic_fee + (((times - basic_time + per_minutes - 1) // per_minutes) * per_fees)

    sort_car_nums = sorted(cars_total_money.items())
    for i in range(len(sort_car_nums)):
        answer.append(sort_car_nums[i][1])

    return answer

## 두번째풀이
## 내 풀이에서 좀더 최적화한 풀이
from collections import defaultdict

END_TIME = 23 * 60 + 59

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees

    car_times = defaultdict(list)

    # 1) 차량별 시각만 수집(차량번호는 문자열 유지)
    for record in records:
        t, car, _ = record.split()
        h, m = map(int, t.split(':'))
        car_times[car].append(h * 60 + m)

    # 2) 누적 시간 계산
    total_time = {}
    for car, times in car_times.items():
        s = 0
        # 2개씩 (in, out) 쌍 계산
        for i in range(0, len(times) - 1, 2):
            s += times[i + 1] - times[i]
        # 홀수면 마지막 in이 남은 것
        if len(times) % 2 == 1:
            s += END_TIME - times[-1]
        total_time[car] = s

    # 3) 요금 계산 + 차량번호 오름차순
    answer = []
    for car in sorted(total_time.keys()):
        t = total_time[car]
        if t <= basic_time:
            fee = basic_fee
        else:
            extra = t - basic_time
            fee = basic_fee + ((extra + unit_time - 1) // unit_time) * unit_fee

        answer.append(fee)

    return answer

## 세번째 풀이 ( 다른 사람 풀이)
## 만약 상태가 여러개일 수도 있을테니 그 상태에 따른 풀이 방식
import math

END_TIME = 23 * 60 + 59
def solution(fees, records):
    check = {}

    for record in records:
        time, number, status = record.split()
        time = time.split(':')
        time = int(time[0]) * 60 + int(time[1])
        if number not in check:
            check[number] = (0, time, status)
        if status == 'IN':
            check[number] = (check[number][0], time, status)
        elif status == 'OUT':
            total_time, in_time, _ = check[number]
            total_time += time - in_time
            check[number] = (total_time, time, status)

    result = {}

    for number in check.keys():
        total_time, time, status = check[number]
        if status == 'IN':
            # 하루의 마지막 시간(23:59)을 분으로 나누면 1439
            total_time += END_TIME - time
        fee = fees[1]
        if total_time <= fees[0]:
            result[number] = fee
        else:
            fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
            result[number] = fee

    return list(map(lambda x: x[1], sorted(result.items())))

## 4번째 풀이(강의풀이)
## 여기도 주차했는지 안했는지 저장하는 변수와 total변수를 따로 만들어놈
## 그리고 정렬을 해야하는데 어차피 차량 범위가 10000안에 있으면 되므로 이렇게 10000개로 하고 하면 정렬을 굳이 안해도 됨
from math import ceil

def convert(string): # '시간: 분'을 데이터로 고쳐서 반환
    h, m = map(int, string.split(':'))
    return 60 * h + m


def get_fee(use_time, basic_time, basic_fee, unit_time, unit_fee):
    if use_time <= basic_time:
        return basic_fee

    total_fee = basic_fee
    use_time -= basic_time
    total_fee += ceil(use_time / unit_time) * unit_fee

    return total_fee


def solution(fees, records):
    total_time = [0] * 10000  # total_time[i]: i번 차가 주차한 시간
    info = [-1] * 10000  # info[i]: i번 차의 주차한 시각 (-1이면 주차하지 않은 상태를 의미)

    # 차량별로 주차한 시간 계산
    for record in records:
        time, num, _ = record.split()
        time = convert(time)
        num = int(num)

        if info[num] != -1:
            total_time[num] += time - info[num]
            info[num] = -1
        else:
            info[num] = time

    for num in range(10000):
        if info[num] != -1:
            total_time[num] += (23 * 60 + 59) - info[num]
            info[num] = -1

    return [get_fee(total_time[num], *fees) for num in range(10000) if total_time[num] != 0]







