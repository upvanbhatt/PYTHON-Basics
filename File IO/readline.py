f=open("demo.txt", "r")
line1= f.readline()
print(line1)

line2= f.readline()
print(line2)


line3= f.readline()
print(line3) # empty space will be printed bcz nothing is left to read

f.close()