for i in range(int(input())): 
    s = input()
    a, b = map(int, input().split())  
    
    if all(char in '01' for char in s):
        count1 = s.count('1')
        count2 = s.count('0')
        count3 = s.count('10')
        count4 = s.count('01')

        if count1 == 0 or count2 == 0:
            print("0")
        elif count3 >= 1 or count4 >= 1:
            if a > b:
                s = '1' * count1 + '0' * count2
                print(b)
            elif a<b:
                s = '0' * count2 + '1' * count1
                print(a)
            else:
                print(a)
                
    else:
        print("INVALID")
