def cal_prod(a=4,b=2): #default parameter
    print(a*b)
    return a*b

cal_prod()

def cal_prod(a,b=2): #default parameter always written in last 
    print(a*b)
    return a*b

cal_prod(2)

# def cal_prod(a=4,b): #error bcz default parameter can't be write in start
#     print(a*b)
#     return a*b

# cal_prod()