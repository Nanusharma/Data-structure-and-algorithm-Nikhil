nums = [1,2]

hash = {}
for i in nums:
    if i in hash:   
        hash[i]+=1
    else:
        hash[i]=1
x = 2
print(hash)
print(type(hash[x]))
