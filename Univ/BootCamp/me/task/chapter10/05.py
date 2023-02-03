# 딕셔너리 만들고 클래스의 객체 생성하기

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}

hydrogen = Element()