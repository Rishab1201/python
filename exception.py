
try :
    num = 2
    demo = 0

    res = num / demo
    print(res)

except ZeroDivisionError:
    print('cannot divide by 0')
finally:
    print("hmmm")