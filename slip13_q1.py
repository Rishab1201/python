class demoexception (Exception):
    pass

try:
    a = int(input('Enter number:'))
    if a < 10:
        raise Exception
except demoexception:
    print('number is invalid')
