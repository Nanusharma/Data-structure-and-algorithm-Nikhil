# By chatgpt{will analyze it later}
# By chatgpt{I'll analyze it later}
def print_hourglass(n):
    # Top half 
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))
    
    # Bottom half 
    for i in range(1, n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


n = 10
print_hourglass(n)
