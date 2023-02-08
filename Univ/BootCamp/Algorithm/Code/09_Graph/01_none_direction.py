## 함수 선언부
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


# 전역 변수부
G1 = None

# 메인 코드부
G1 = Graph(4)
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[1][3] = 1
G1.graph[2][2] = 1
G1.graph[3][0] = 1
G1.graph[3][1] = 1

print('-- None Direction Graph --')
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end=' ')
    print()
