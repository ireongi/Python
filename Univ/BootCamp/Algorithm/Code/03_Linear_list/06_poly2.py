## 함수 선언 부분 ##

def print_poly(px, tx):
    """
    다항식을 포맷에 맞게 출력하는 함수
    :param px: 계수를 원소로 가지고 있는 List
    :param tx: 차수를 원소로 가지고 있는 List
    :return: 다항식 문자열
    """
    poly_str = "P(x) = "

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        if coef >= 0:
            poly_str = poly_str + "+"

        poly_str = poly_str + f'{coef}x^{term} '

    return poly_str


def calc_poly(x_val, px, tx):
    """
    다항식의 산술연산
    :param x_val: x값 integer
    :param px: 계수를 원소로 가지고 있는 list
    :param tx: 차수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 integer
    """
    return_val = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        return_val = return_val + coef * x_val ** term

    return return_val


## 전역 변수 선언 부분 ##
px = [3, -4, 5]
tx = [300, 20, 0]

## 메인 코드 부분 ##
if __name__ == "__main__":
    print(print_poly(px, tx))

    x_value = int(input("X 값 : "))
    print(calc_poly(x_value, px, tx))


