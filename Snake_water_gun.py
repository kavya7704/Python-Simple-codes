n = int(input())
arr = []
for _ in range(n):
    element = input()
    arr.append(element)
    
def Game(n,arr):
    count = 0
    rules = {'snake':'water','water':'gun','gun':'snake'}
    for i in range(n):
        moves = arr[i]
        rounds = []
        temp = ""
        for char in moves:
            temp += char
            if temp in rules :
                rounds.append(temp)
                temp = ""
        player_a_wins = 0
        for j in range(0,len(rounds),2):
            if j + 1 < len(rounds):
                player_a = rounds[j]
                player_b = rounds[j+1]
                if rules[player_a] == player_b:
                    player_a_wins += 1
    count += player_a_wins
    return count
    
print(Game(n,arr))
