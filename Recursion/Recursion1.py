# Recursion:When a function calls itself repeatedly
#Recursive function
def show(n):
    if(n==0): #Base case :- it decides recursion should stop or not
        return
    print(n)
    show(n-1)
    print("END")

show(5) #5,4=n-1, 3=n-2, 2=n-3, 1=n-4
