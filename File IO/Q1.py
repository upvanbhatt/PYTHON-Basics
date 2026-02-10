# create a new file "practical.txt" using python .
#Add the following data in it
# Hi everyone
# we are learning File I/O
# using java.
# I like programming in java
with open("practice.txt", "w") as f: #w mode automatically create the file
    f.write("Hi everyone\nWe are learning File I/o\n ")
    f.write("using java.\nI like programming in java.")