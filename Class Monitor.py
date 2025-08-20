'''After JEE Mains, some students got admission into an engineering college. Now there is a class consisting of such n students, and the HOD came to say it is time to select the class monitor. But He never gets all of them at one time. So he brought a register, every time he gets someone with less rank than the previous time he cut the name and wrote the name of the student and the rank.
For a given number of ranks he gets each time, you have to predict how many names are cut in the list.'''

N = int(input())
Rank = list(map(int, input().split()))

def Monitor(N,Rank):
    count = 0
    
    for i in range(1,N):
        elif Rank[i] < Rank[i-1]:
            count += 1
        
    return count
    
print(Monitor(N,Rank))
