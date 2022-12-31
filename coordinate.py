import math

x1 = int(input('Enter coordinate X1:'))

y1 = int(input("Enter coordinate Y1:"))

x2 = int(input("Enter coordinate X2:"))

y2 = int(input("Enter coordinate Y2:"))

ans = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

print('Ans:',ans)