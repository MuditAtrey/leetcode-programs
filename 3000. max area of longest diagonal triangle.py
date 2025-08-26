def areaOfMaxDiagonal(dimensions)
    if sqrt((dimensions[0][0]**2)+(dimensions[0][1]**2))>sqrt((dimensions[0][0]**2)+(dimensions[0][1]**2)):
        return dimensions[0][0]*dimensions[0][1]
    else:
        return dimensions[1][0]*dimensions[1][1]
    x=0
    y=0
    for i in range(len(dimensions)):
        if sqrt((dimensions[i][0]**2)+(dimensions[i][1]))>x:
            x=sqrt((dimensions[i][0]**2)+(dimensions[i][1]))
            y=i
    return dimensions[y][0]*dimensions[y][1]
print areaOfMaxDiagonal([[4,10],[4,9],[9,3],[10,8]])