def divide(dividend: int, divisor: int) -> int:
    b, x = 1, 0


    y = False
    z = False

    if dividend < 0:
        dividend = 0 - dividend
        y = True
    if divisor < 0:
        divisor = 0 - divisor
        z = True
    c=divisor
    if divisor == 1:
        x = dividend
    else:
        while (c << 1) <= dividend:
            c <<= 1
            b <<= 1
        while dividend >= divisor:
            if dividend >= c:
                dividend -= c#1
                x += b#3
            c >>= 1#1
            b >>= 1#0

    if y:
        x = 0 - x
    if z:
        x = 0 - x
    if x > 2147483647:
        x -= 1
    return x
print(divide(10,-3))