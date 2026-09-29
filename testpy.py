for i in range(1, 3):
    x = input('Hi please enter the name: ').upper()
    if x == 'SAJJAD':
        print('hello the genius ' + x)
    else:
        print('hello ' + x)
        
    with open("temp", "a") as f:
        f.write(x + "\n")
