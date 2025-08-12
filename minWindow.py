def minWindow(s, t):
    if not s or not t:
        return ""

    need = [0] * 128
    have = [0] * 128
    
    for ch in t:
        need[ord(ch)] += 1  
    
    required = len(t)  
    left = 0
    min_len = float("inf")
    min_start = 0
    
    for right in range(len(s)):
        ch = s[right]
        have[ord(ch)] += 1
        
       
        if have[ord(ch)] <= need[ord(ch)]:
            required -= 1
        
       
        while required == 0:
            
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                min_start = left
            
            have[ord(s[left])] -= 1
            if have[ord(s[left])] < need[ord(s[left])]:
                required += 1
            left += 1
    
    return "" if min_len == float("inf") else s[min_start:min_start + min_len]


# Example
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  
