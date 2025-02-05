def fxn1(S: str) -> list:
    count = 1
    ar = []
    
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            count += 1
        else:
            ar.append([count, int(S[i-1])])
            count = 1
            
    # Handle the last group
    ar.append([count, int(S[-1])])
    
    return ar

print(fxn1("3322251"))
print(fxn1("1211"))