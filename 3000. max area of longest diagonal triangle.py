class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        x=0
        y=0
        print(len(dimensions))
        for i in range(0,len(dimensions)):
            if sqrt((dimensions[i][0]**2)+(dimensions[i][1]**2))>=x:
                if x<sqrt((dimensions[i][0]**2)+(dimensions[i][1]**2)):
                    x=sqrt((dimensions[i][0]**2)+(dimensions[i][1]**2))
                    y=i
                    continue
                
                if x==sqrt((dimensions[i][0]**2)+(dimensions[i][1]**2)):
                    print(i)
                    if dimensions[y][0]*dimensions[y][1]<dimensions[i][0]*dimensions[i][1]:
                        x=sqrt((dimensions[i][0]**2)+(dimensions[i][1]**2))
                        print(i)
                        continue

                    else:
                        continue
                

        
        return dimensions[y][0]*dimensions[y][1]

        