class Pokemon:
    def __init__(self, owner, name) -> None:
        self.owner = owner
        self.name = name
        self.is_hanjiwoo()

    def is_hanjiwoo(self) -> bool:
        if self.owner == '한지우':
            return True
        else:
            return False


def find_hanjiwoos(monsters) -> list:
    for monster in monsters:
        if monster.owner == "한지우":
            hp_list.append(monster.name)
    return hp_list


def my_sort(arr, arr2, start, end) -> None:
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low + high) // 2]  # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리한다.
    while low <= high:
        while arr[low] > pivot:
            low += 1
        while arr[high] < pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            arr2[low], arr2[high] = arr2[high], arr2[low]
            low, high = low + 1, high - 1

    mid = low

    my_sort(arr, arr2, start, mid - 1)
    my_sort(arr, arr2, mid, end)


pokemons = [
    Pokemon("한지우", "피카츄"),
    Pokemon("오바람", "꼬부기"),
    Pokemon("나이기", "파이리"),
    Pokemon("한지우", "파이리"),
    Pokemon("덴트", "메더"),
    Pokemon("덴트", "암팰리스"),
    Pokemon("나이기", "리자드"),
    Pokemon("아이리스", "터검니"),
    Pokemon("한지우", "이상해")
]

hp_list = []

if __name__ == "__main__":
    counts = dict()

    for pokemon in pokemons:
        print(f'{pokemon.name}의 주인은 {pokemon.owner}입니다.')

    hanjiwoo_pokemons = find_hanjiwoos(pokemons)
    hp = []
    for hanjiwoo_pokemon in hanjiwoo_pokemons:
        hp.append('지우 포켓몬 : ' + hanjiwoo_pokemon)
    print(hp)

    for i in range(0, len(pokemons)):
        counts[pokemons[i].owner] = 0

    for i in range(0, len(pokemons)):
        counts[pokemons[i].owner] += 1
    owner_list = list(counts.keys())
    name_list = list(counts.values())

    print("===정렬 전===")
    for i in range(0, len(owner_list)):
        print(f'{owner_list[i]} 소유 포켓몬은 총 {counts[owner_list[i]]}마리 입니다.')

    my_sort(name_list, owner_list, 0, len(counts) - 1)

    print("===정렬 후===")
    for i in range(0, len(owner_list)):
        print(f'{owner_list[i]} 소유 포켓몬은 총 {counts[owner_list[i]]}마리 입니다.')
