def Tower_Hanoi(n,s,a,d):
    
    if n == 1:
        print(f"Move disk 1 from {s} to {d}")
        return 
    Tower_Hanoi(n-1,s,d,a)
    print(f"Move disk {n} from {s} to {d}")

    Tower_Hanoi(n-1,a,s,d)

n = 3

Tower_Hanoi(n,'A','B','C')