# Element 클래스에서 값을 출력하는 dump()에서 정의, hydrogen 객체 생성, dump() 메서드로 이 속성을 출력

class Element():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

hydrogen = Element()
hydrogen.name = 'Hydrogen'
hydrogen.symbol = 'H'
hydrogen.number = 1

hydrogen.dump()

print(hydrogen)