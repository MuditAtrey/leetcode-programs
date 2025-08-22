class Solution:
    def romanToInt(self, s: str) -> str:
        
        x=0   
        i=0   
        while i<len(s):
            if s[i]=="I":
                if (i+1)<len(s) and s[i+1]=="I":
                    if (i+2)<len(s) and s[i+2]=="I":
                        x+=3
                        break
                    x+=2
                    break
                if (i+1)<len(s) and s[i+1]=="X":
                    x+=9
                    i+=2
                    continue
                if (i+1)<len(s) and s[i+1]=="V":
                    x+=4
                    i+=2
                    continue
                else:
                    x+=1  
                    i+=1
                    continue          
            if s[i]=="V":
                x+=5
                i+=1
                continue
            if s[i]=="X":
                if (i+1)<len(s) and s[i+1]=="L":
                    x+=40
                    i+=2
                    continue
                if (i+1)<len(s) and s[i+1]=="C":
                    x+=90
                    i+=2
                    continue
                else:
                    x+=10 
                    i+=1
                    continue
            if s[i]=="L":
                x+=50
                i+=1
                continue
            if s[i]=="C":
                if (i+1)<len(s) and s[i+1]=="D":
                    x+=400
                    i+=2
                    continue
                if (i+1)<len(s) and s[i+1]=="M":
                    x+=900
                    i+=2
                    continue
                else:
                    x+=100
                    i+=1
                    continue
            if s[i]=="D":
                x+=500
                i+=1
                continue
            if s[i]=="M":
                x+=1000
                i+=1
                continue
        return x


        
