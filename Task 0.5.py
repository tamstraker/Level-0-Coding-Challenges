# Python program to find the area of a triangle

def areaoftriangle(s1,s2,s3):
    
    #sides of triangle are s1, s2 and s3
    s1 = float(input("Enter the first side: "))
    "Enter the first side: 6"

    s2 = float(input("Enter the second side: "))
    "Enter the second side: 8"

    s3 = float(input("Enter the third side: "))
    "Enter the third side: 10"

    #calculate semi-perimeter
    s = (s1 + s2 + s3) / 2

    #calculate the Area
    Area = (s * (s - s1) * (s-s2) * (s-s3)) ** 0.5
    
    print("The Area of a triangle is: %0.2f" %Area)
    print(areaoftriangle(6,8,10))


