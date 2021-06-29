sideA= int(input("Length of side a:" ))
sideB= int(input("Length of side b:" ))
sideC= int(input("Length of side c:" ))
if sideA == sideB or sideA == sideC:
    print ("The tringe is an equilateral")
elif sideB == sideC:
    print ("The triangle is an equilateral")
else:print ("The Triangle is not an equilateral")
