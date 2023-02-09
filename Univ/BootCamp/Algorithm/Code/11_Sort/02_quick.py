import random

## 함수 선언 부분 ##
def quick_sort(array):
    global count
    n = len(array)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return array

    pivot = array[n // 2]  # 기준값을 중간값으로 지정
    left_array, right_array = [], []

    for num in array:
        if num > pivot:
            left_array.append(num)
            count += 1
        elif num < pivot:
            right_array.append(num)
            count += 1

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


## 전역 변수 선언 부분 ##
data_array = [random.randint(0, 100) for _ in range(5)]
count = 0

## 메인 코드 부분 ##
print('정렬 전 -->', data_array)
data_array = quick_sort(data_array)
print('정렬 후 -->', data_array)
print(f'정렬 실행 횟수 : {count}')
