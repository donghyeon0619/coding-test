"""
좌표 압축 concept
: 큰 범위의 수들을 작은 범위의 수들로 변환하는 것을 의미함
- 좌표 압축을 하면 살펴봐야 하는 수의 범위를 줄일 수 있음
- 숫자들의 대소 관계만 비교해도 되는 경우에 좌표압축 사용 가능
- 좌표 압축을 하면 최대 N개의 숫자의 범위를 가지게 됨
- 만약에, 중복된 원소가 있다면 N개보다 더 작은 범위를 가진다.
"""
arr = [324, 132, 3, 23, 12, 575, 984, 14] # 원래 배열
print(arr)

N = len(arr)

# Coordinate Compression - start
nums = sorted(set(arr)) # O(N logN)

convert = dict()
# enumerate() 함수는 배열의 원소와 인덱스를 함께 사용가능,
# 두번째 매개변수에 값을 넣으면 해당 값부터 인덱스가 시작
# 만약 10을 넣으면 10부터 시작하게 됨
for idx, num in enumerate(nums, 1):
    convert[num] = idx

for i in range(N):
    arr[i] = convert[arr[i]]

# Coordinate Compression - end

print(arr)

