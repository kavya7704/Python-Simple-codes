'''Every decimal number can be changed into its binary form. Suppose your computer has it’s own CoronaVirus, that eats binary digits from the right side of a number. Suppose a virus has 6 spikes, it will eat up 6 LSB binary digits in your numbers.
You will have a bunch of numbers, and your machine will have a virus with n spikes, you have to calculate what will be the final situation of the final numbers.'''

N = int(input())
arr = list(map(int,input().split()))
S = int(input())

def Corona(N,arr,S):
    m = ""
    for i in arr:
        m += str(i>>S) + ""
    return m
print(Corona(N,arr,S))
