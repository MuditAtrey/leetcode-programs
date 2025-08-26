#498 diagonal traverse
def fin(mat):
    i,j=0,0
    R=-1
    Q=[]
    m=len(mat)
    n=len(mat[0])
    while i<m and j<n:
        if i==m-1 and j==n-1:
            Q.append(mat[i][j])
            break
        if i==0 and R==-1 and j!=n-1:
            Q.append(mat[i][j])
            j+=1
            R=1
            continue
        if i==m-1 and R==1 and j!=n-1:
            Q.append(mat[i][j])
            j+=1
            R=-1
            continue
        if j==0 and R==1 and i!=m-1:
            Q.append(mat[i][j])
            i+=1
            R=-1
            continue
        if j==n-1 and R==-1 and i!=m-1:
            Q.append(mat[i][j])
            i+=1
            R=1
            continue

        if R==1:
            Q.append(mat[i][j])
            i+=1
            j-=1
        if R==-1:
            Q.append(mat[i][j])
            i-=1
            j+=1




    return Q
print(fin([[1,2],[4,5],[7,8]]))
