## Kruskal Algorithm ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print('  ', end=' ')
    for v in range(g.SIZE):
        print(name_array[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(name_array[row], end=' ')
        for col in range(g.SIZE):
            print("%2d" % g.graph[row][col], end=' ')
        print()
    print()


def find_vertex(g, findVtx):
    stack = []
    visited_array = []  # 방문한 노드

    current = 0  # 시작 정점
    stack.append(current)
    visited_array.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visited_array:  # 방문한 적이 있는 정점이면 탈락
                    pass
                else:  # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break

        if next != None:  # 다음에 방문할 정점이 있는 경우
            current = next
            stack.append(current)
            visited_array.append(current)
        else:  # 다음에 방문할 정점이 없는 경우
            current = stack.pop()

    if findVtx in visited_array:
        return True
    else:
        return False


## 전역 변수 선언 부분 ##
G1 = None
name_array = [' a', ' b', ' c', ' d', ' e', ' f']
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5

## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[a][b] = 10; G1.graph[a][c] = 15;
G1.graph[b][a] = 10; G1.graph[b][c] = 40; G1.graph[b][d] = 11; G1.graph[b][e] = 50
G1.graph[c][a] = 15; G1.graph[c][b] = 40; G1.graph[c][d] = 12
G1.graph[d][b] = 11; G1.graph[d][c] = 12; G1.graph[d][e] = 20; G1.graph[d][f] = 30
G1.graph[e][b] = 50; G1.graph[e][d] = 20; G1.graph[e][f] = 25
G1.graph[f][d] = 30; G1.graph[f][e] = 25

print('------- Graph -------')
print_graph(G1)

# 가중치 간선 목록
edge_array = []
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k] != 0:
            edge_array.append([G1.graph[i][k], i, k])

from operator import itemgetter

edge_array = sorted(edge_array, key=itemgetter(0), reverse=True)

new_array = []
for i in range(0, len(edge_array), 2):
    new_array.append(edge_array[i])

index = 0
while (len(new_array) > gSize - 1):  # 간선의 개수가 '정점 개수-1'일 때까지 반복
    start = new_array[index][1]
    end = new_array[index][2]
    saveCost = new_array[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = find_vertex(G1, start)
    endYN = find_vertex(G1, end)

    if startYN and endYN:
        del (new_array[index])
    else:
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

print('----- New Graph -----')
print_graph(G1)
