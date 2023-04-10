
queue = []

def enqueue():
    n = int(input('Enter how many values you want to enter :- '))

    for i in range(n):
        value = int(input('Enter value:'))
        queue.append(value)

    print(queue)


def isempty():
    if len(queue) == 0:
        print('your queue is empty')

def dequeue():
    if isempty():
        return 0
    else:
        queue.pop(0)
    print(queue)


while(1):
    print('1.Enter value in queue')
    print('2.delete value from queue')
    print('3.exit')
    ch = int(input('Enter your choise :-'))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        exit()