# insert 내부구조 구조

def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon

# main 함수처럼 만들기
if __name__ == "__main__" :
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

    print(pokemons)
    insert_data(2, '거북왕') # 9번행 실행되면서 빈칸 생김(6번방)
    print(pokemons)
    insert_data(6, '어니부기') # 19행 실행 후 6번방에 값 넣기 가능
    print(pokemons)
    # pokemons.insert(6, '어니부기') 빌트인 기능 사용

