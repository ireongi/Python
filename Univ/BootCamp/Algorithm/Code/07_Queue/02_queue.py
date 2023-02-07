## 함수 선언 부분 ##
def is_queue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("Queue is Full!")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("Queue is EMPTY~")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("Queue is EMPTY~")
        return None
    return queue[(front + 1) % SIZE]


## 전역 변수 선언 부분 ##
SIZE = int(input("Input Queue SIZE ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__":
    select = input("Insert(I)/Extrack(E)/Verify(V)/eXit(X)  ==> ")

    while select != 'X' and select != 'x':
        if select == 'I' or select == 'i':
            data = input("Input Data ==> ")
            en_queue(data)
            print("Queue Status : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = de_queue()
            print("Check Data ==> ", data)
            print("Queue Status : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("Check Data ==> ", data)
            print("Queue Status : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("Input mismatch")

        select = input("Insert(I)/Extrack(E)/Verify(V)/eXit(X)  ==> ")

    print("Program End")
