N, M = map(int, input().split())
pokemons = {}
idx = []
for i in range(N):
    pokemon = input()
    pokemons[i] = pokemon
    pokemons[pokemon] = i
#print(pokemons)
for j in range(M):
    quiz = input()
    if '0' <= quiz[0] <= '9':
        quiz = int(quiz) - 1
        print(pokemons[quiz])
    else:
        print(pokemons[quiz] + 1)