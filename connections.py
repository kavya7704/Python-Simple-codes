from collections import defaultdict

n, m = map(int, input().split())
connections = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

K = int(input())


current_state = [1] * n  

roster = n
day = 1

while roster < K:
    next_state = [0] * n  
    
    for emp in range(n):
        wfo_friends = sum(current_state[friend] for friend in connections[emp])
        
        if current_state[emp] == 1:  
            if wfo_friends == 3:
                next_state[emp] = 1
        else:  
            if wfo_friends < 3:
                next_state[emp] = 1
    
    
    current_state = next_state
    roster += sum(current_state)
    day += 1

print(day)