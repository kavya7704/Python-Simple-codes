def substring(s):
    arr = []
    curr = ""
    for i in s:
        if i.isdigit():
            curr += i
        else:
            if curr:
                arr.append(curr)
                curr = ""
            
    if curr:
        arr.append(curr)
    print(arr)
    count = 0
    for i in range(0,len(arr) - 2):
        if arr[i][-1] != arr[i+1][0]:
            count += 1
            
    return count
    
s = "input()" #abc123cd45ef67gh8

print(substring(s)) #3
