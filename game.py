n = 10
y = 11

upper_part = []


for i in range(n):
    line = " " * (n - i - 1)  
    if i == 0:
        line += "1"
    elif i == 1:
        line += "11"
    else:
        y *= 11
        line += str(y)
    upper_part.append(line)

# Print the upper part
for line in upper_part:
    print(line)

# Print the lower part (reverse of the upper part, excluding the middle line)
for line in reversed(upper_part[:-1]):
    print(line)
