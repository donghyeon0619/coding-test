# 나이순 정렬
# sort는 timsort이므로 n log n 밖에 안걸림
# 여기서는 key 매개변수에 x[0]의 오름차순으로 정렬
import sys

readline = sys.stdin.readline

n = int(readline())
arr = []
for i in range(n):
    arr.append(list(readline().split()))

sorted_arr = sorted(arr, key=lambda x: int(x[0]))

print("\n".join(map(" ".join, sorted_arr)))
# 같은 방법
# for i in range(len(sorted_arr)):
#     print(sorted_arr[i][0], sorted_arr[i][1])


# 두번째 풀이 (다른사람 풀이)
# 메모리 적으로나 시간적으로 효율적으로 아끼는 법
# 입력값들을 전부 readlines()를 이용해서 전부 입력받음 각 리스트들은 \n이 포함되어있음
import sys

name_list = sys.stdin.readlines()[1:]

name_list.sort(key=lambda x: int(x.split()[0]))

print("".join(name_list))