largest = None
smallest = None

while True :
    try:
        num = input('Enter a number:')
        if num == 'done' :
        break
        n = int(num)
        if largest < n:
            largest = n
        if smallest > n:
            smallest = n

    except:
        print('Invalid Input')
        continue


print('Maximum is', largest)
print('Smallest is', smallest)
