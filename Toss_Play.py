s = input()

def Toss(s):
    final_score = 0
    count = 0
    for i in s:
        if count == 3:
            return final_score
            break
        elif i == "H":
            final_score += 2
            count += 1
        elif i == "T":
            final_score -= 1
            count = 0
    return final_score
print(Toss(s))
