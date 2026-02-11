#WAF to find in which line of the file does the word "learning" occure first. Print 1 if the word not found.

def check_for_word():
    word="xlearning"
    with open ("practice.txt", "r") as f:
       data=f.read()

       if (word in data):
            print("Found")
       else:
            print("not found")



def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open ("practice.txt", "r") as f:
        while data:
            data= f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1

    return-1
print(check_for_line())