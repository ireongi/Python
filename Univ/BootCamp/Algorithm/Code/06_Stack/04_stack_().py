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


def check_bracket(expression):
    for ch in expression:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass  # 괄호가 아니면 지나감
    if is_stack_empty():
        return True
    else:
        return False


## 전역 변수 선언 부분 ##
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__":

    expression_array = ['2*[3+1', '()', ')(', '(()-', '(]', '(<+{}/[]>)']

    for expr in expression_array:
        top = -1
        print(expr, ' : ', check_bracket(expr))
