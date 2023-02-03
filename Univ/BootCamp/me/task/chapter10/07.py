# Element 클래스에서 dump 메서드를 __str__() 메서드로 변경하여 새 hydrogen 객체를 생성, print(hydrogen)을 호출

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return self.name+self.symbol+self.number

hydrogen = Element('d','f','e')
print(hydrogen)
