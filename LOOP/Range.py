#Range function return a sequence of numbers, starting from 0 by default
# range( start, stop, step)
print (range(5))

#loop
seq= range(10) # range(stop)
for i in seq:
    print(i)
print("end")

for i in range(2,10): #range (start, stop)
    print(i)
print("end")

for i in range(2,10, 2): #range (start, stop, step)
    print(i)
print("end")

#even number

for i in range(2,101,2): #range (start, stop, step)
    print(i)