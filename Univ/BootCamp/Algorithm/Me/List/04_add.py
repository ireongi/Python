

def insert_data(index, pokemon):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons) - 1, index, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[index] = pokemon #
    """
    선형 리스트의 idx위치에 원소 삽입
    :param pokemon:
    """
def delete_data(index):
    if index < 0 or index > len(pokemons):
        print("Out of range!")
        return

    len_pokemons = len(pokemons) #python에서 kLen같은 표기는 지양
    pokemons[index] = None  # 데이터 삭제

    for i in range(index + 1, len_pokemons):
      pokemons[i - 1] = pokemons[i]
    pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_pokemons - 1])
    """
    선형 리스트의 
    :pram index:
    :param pokemon:
    
    """
def add_data(pokemon):
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon
    """
    선형 리스트의 맨 뒤에 원소 삽입
    :param pokemon
    """

if __name__ == "__main__" :
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]

    print(pokemons)
    delete_data(1)
    print(pokemons)
    add_data('터검니')
    print(pokemons)

