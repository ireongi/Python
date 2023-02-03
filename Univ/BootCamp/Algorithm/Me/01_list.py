# 배열 만들기

pokemons = []  # 빈 배열, 배열명은 복수형으로 쓰는게 좋음

def add_data(pokemon):
    pokemons.append(None)  # 빈 공간 생성(최초, 0번방)
    # pokemons[len(pokemons) - 1] = pokemon # len(pokemons) = 1 이므로 0번방에 넣기위해 -1
    pokemons[-1] = pokemon


add_data('피카츄')
add_data('라이츄')
add_data('원츄')
add_data('꼬부기')
add_data('이상해')

print(pokemons)
