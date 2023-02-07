queue = [None for _ in range(5)]
front = rear = -1

rear += 1
queue[rear] = "가"
rear += 1
queue[rear] = "나"
rear += 1
queue[rear] = "다"

print('<- 나가는 문|', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ~ ')
print('<- 들어오는 문|')
