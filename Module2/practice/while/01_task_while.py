a = int(input("Please enter the value for a"))
b = int(input("Please enter the value for b"))
if b < a :
    print ("a is already bigger than b")
else:
    while a<b-1:
        a += 1
        print (a)
