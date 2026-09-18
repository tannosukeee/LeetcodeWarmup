def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)


countdown(5)

def countdown_iterative(n):
    while n > 0:
        print(n)
        n -= 1
        
countdown_iterative(5)