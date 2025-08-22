def myatoi(s: str) -> int:
    numbers=""
    digits="0123456789"
    checknum=1
    for i in range(len(s)):
        if s[i]==" " and checknum==1:
            continue

        if s[i] in digits or  ((s[i]==" " or s[i]=="-" or s[i]=="+") and checknum==1):
            numbers+=s[i]
            checknum=-1
        else:
            break
    try:
        numbers=int(numbers)
    except(ValueError):
        numbers=0
    if numbers<-2147483648:
        numbers=-2147483648
    if numbers>2147483647:
        numbers=2147483647

    return numbers
print(myatoi("+1337 4- cd023"))