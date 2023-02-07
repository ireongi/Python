import webbrowser
import time


## 함수 선언 부분 ##
def is_stack_full():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    return False


def is_stack_empty():
    global SIZE, stack, top
    if top == -1:   # top이 없으면
        return True
    return False


def push(data):
    global SIZE, stack, top
    if is_stack_full():
        print("Stack is FULL!")
        return
    top = top + 1
    stack[top] = data


def pop():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY~")
        return
    temp = stack[top]
    stack[top] = None
    top = top - 1
    return temp


def peek():
    global SIZE, stack, top
    if is_stack_empty():
        print("Stack is EMPTY~")
        return
    return stack[top]


## 전역 변수 선언 부분 ##
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__":
    urls = ['inha.ac.kr', 'harvard.edu', 'yale.edu']

    for url in urls:
        push(url)
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1) # 1초 쉬고

    print("End")
    time.sleep(5)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('http://' + url)
        print(url, end='-->')
        time.sleep(1)
    print("End")
