a = int(input("Enter outer radius of ring:"))

b = int(input("Enter inner radius of ring:"))

perimeter = 2 * 3.14 * (a + b)

print("Perimeter of ring-->",perimeter)

area = 3.14 * (a**2 - b**2)

print("Area of ring-->",area)