#WAF to print the elements of a list in a single line.(list is the parameter)
fruit=["apple", "banana", "mango", "grapes"]
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(fruit)
print() #to remove % sign
