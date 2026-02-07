f=open("demo.txt", "r")

data=f.read()
print(data)

line1= f.readline() #empty space bcz data is already read so nothing left to read
print(line1)

line2= f.readline()
print(line2)

f.close()