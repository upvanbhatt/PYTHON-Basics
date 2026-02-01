# Wap to find the factorial of first n numbers (using for )
n=int(input("enter number:"))
fact=1
i=1
while i<=n:
    fact *= i
    i += 1

print("factorial =",fact)

#for loop
n=int(input("enter number:"))
fact= 1
for i in range (1, n+1):
    fact *= i
print("factorial =", fact)