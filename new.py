def strongPass(password):
    low,up,dig=-1,-1,-1
    check=0
    trip=password
    tripn=0
    tripc=0
    add=0
    sub=0
    rep=0
    changes=0


    for i in range(len(password)):
        if password[i]*3 in trip:
            temp=len(trip)
            trip=trip.replace(password[i]*3,"")
            tripn+=((temp-len(trip))//3)
            rep=tripn
        if password[i].islower():
            low=1
        if password[i].isupper():
            up=1
        if password[i].isdigit():
            dig=1
        """
        if password[i]*3 in trip and password[i].isdigit()==True :
            temp=len(trip)
            trip=trip.replace(password[i]*3,"")
            tripc+=((temp-len(trip))//3)
        """
    print(tripn,tripc,changes)

    if low==-1:
        add+=1
        pass
    if up==-1:
        add+=1
        pass
    if dig==-1:
        add+=1
        pass
    if len(password)<6:
        add=len(password)-6 #A1234
    if len(password)>20:
        sub=20-len(password)


    if changes>0 and tripn>0:
        for i in range(changes):
            tripn-=1
            if tripn==0:
                break
    print(tripn,changes)




    """
    if low==-1:
        #print("j"), HHHHHH
        changes+=1
        if tripn>0:
            changes-=1
            tripn-=1
        elif tripc>0:
            tripc-=1
            changes-=1

    if up==-1:
        print("j")
        print(changes)
        changes+=1
        if tripn > 0 and changes>1:
            changes -= 1
            tripn -= 1
            #print(changes)
        elif tripc > 0 and changes>1:
            tripc -= 1
            changes -= 1
        print("coom",tripc,tripn,changes)

    if dig==-1:
        changes+=1
        if tripn>0 and changes>1:
            changes-=1
            tripn-=1

    print(changes)
    if tripc>0:
        changes+=tripc
    print(changes,tripn)
    if tripn>0:
        changes+=tripn
    print(changes,tripc,tripn)

    """

    if len(password) < 6 or len(password) >20:
        if len(password)<6:
            if changes>(6-len(password)):#222 1+1=2 1
                if tripn!=0:

                    return (6-len(password))+(changes-(6-len(password)))+1
            else:
                return 6-len(password)
        if len(password) > 6:
            if changes > (len(password)-20):

                return (len(password)-20) + (changes - (len(password)-20))
            else:
                return len(password)-20


    if changes>0:
        return changes
    else:
        return 0

print(strongPass("111"))

#note, the entire code needs a rework, stop trying to retrofit new conditions into it