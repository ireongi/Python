

if __name__ == "__main__":
    pokemons = [{'피카츄': 150}, {'라이츄': 130}, {'파이리': 110}, {'꼬부기': 100}, {'버터플': 80}]

    pokemons.append(None)

    print(pokemons)

    del(pokemons[len(pokemons)-1])

    print(pokemons)
