def strongPass(passw):
    low,up,dig=-1,-1,-1
    check=0
    trip=passw
    tripn=0
    changes=0


    for i in range(len(passw)):
        if passw[i]*3 in trip and passw[i].isdigit()==False:
            temp=len(trip)
            trip=trip.replace(passw[i]*3,"")
            tripn+=((temp-len(trip))//3)
        if passw[i].islower():
            low=1
        if passw[i].isupper():
            up=1
        if passw[i].isdigit():
            dig=1


    if low==-1:
        changes+=1
        if tripn>1 and changes>1:
            changes-=1
            tripn-=1
            check+=1
    if up==-1:
        changes+=1
        if tripn>1 and changes>1:
            changes-=1
            tripn-=1
            check+=1
    if dig==-1:
        changes+=1
        if tripn>1 and changes>1:
            changes-=1
            tripn-=1
            check+=1

    if len(passw) < 6 or len(passw) >20:
        if len(passw)<6:
            if changes>(6-len(passw)):
                if tripn!=0:

                    return (6-len(passw))+(changes-(6-len(passw)))+1
            else:
                return 6-len(passw)
        if len(passw) > 6:
            if changes > (len(passw)-20):

                return (len(passw)-20) + (changes - (len(passw)-20))
            else:
                return len(passw)-20


    if changes>0:
        return changes
    else:
        return 0

print(strongPass("aaa"))

#note, the entire code needs a rework, stop trying to retrofit new conditions into it