def noobish_monk(a,b,c):
    number=[a,b,c]
    for i in range(5):
        smallest= number.index(min(number))
        number[smallest]+=1
    max_product = 1
    for num in number:
        max_product*=num
    return max_product



