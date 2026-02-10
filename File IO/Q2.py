#WAF that replaces all occurrences of "Java" with "Python" in above file.
with open("practice.txt", "r") as f:
    data= f.read()

new_data= data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f: # for overwrite
    data= f.write(new_data)