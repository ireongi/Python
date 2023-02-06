# p195 응용 예제1
# 현 위치(0,0) 편의점 10곳 위치_튜플(x,y) x, y 값 랜덤하게 1~100까지
# 현 위치에서 편의점까지의 거리는 제곱근의 더하기로 계산(x^x + y^y)

# 설계
# 1. 현 위치 설정 / 2. 편의점 10곳 위치 랜덤 생성 & 튜플로 받기 / 3. 현 위치와 편의점 거리 계산 함수 생성 / 4. 거리에 따른 원형 리스트 생성
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


def print_node(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def sort_mart():
    for i in range(0, len(mart_location)):
        for k in range(0, len(mart_location)):
            if mart_distance[i] > mart_distance[k]:
                mart_distance[i] = mart_distance[k]


def random_mart():
    for _ in range(10):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        mart_location.append((x, y))


def how_far_mart():
    for i in range(0, len(mart_location)):
        pair = mart_location[i]
        mart_distance.append((pair[0] * pair[0]) + (pair[1] * pair[1]))
    return


head, current, pre = None, None, None
mart_location = []
mart_distance = []

if __name__ == "__main__":
    random_mart()
    how_far_mart()
    print(mart_location)
    print(mart_distance)

    print(mart_distance)
