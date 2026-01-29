i=0
while i<= 5:
    if (i==3):
        i+=1 # i=3:- 3+1=4
        continue # skip
    print(i)
    i +=1

    # odd number
    i= 1
    while i<=10:
        if(i % 2==0):
            i+=1
            continue
        print(i)
        i+=1

#even number
    i= 1
    while i<=10:
        if(i % 2!=0):
            i+=1
            continue
        print(i)
        i+=1
    