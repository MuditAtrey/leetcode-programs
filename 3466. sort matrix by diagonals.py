def matrix(grid): #3446
    n=len(grid)

    for i in range(n-2,-1,-1):
        #print(i)
        k=0
        a=[]
        for j in range(i,n):
            a.append(grid[j][k])
            k+=1

        for l in range(1,len(a)):
            key=a[l]
            m=l-1
            while m>=0 and key>a[m]:
                a[m+1] =a[m]
                m-=1
            a[m+1]=key
        for j in range(n-1,i-1,-1):
            k-=1
            #print(j)
            grid[j][k]=a[k]
        #print(a)
        #print(grid)


    for j in range(1,n-1):
        k=0
        a=[]
        for i in range(j,n):
            a.append(grid[k][i])
            #print("jump",i)
            k+=1
        #print(a)
        for l in range(1,len(a)):
            key=a[l]
            m=l-1
            while m>=0 and key<a[m]:
                a[m+1] =a[m]
                m-=1
            a[m+1]=key
        for i in range(n - 1, j - 1, -1):
            k-=1
            grid[k][i]=a[k]

        #print(a,grid)
    return grid

print(matrix([[1]]))