# prompt for hours and rate to compute pay with overtime calculation
# catching exceptions with try and except

try:
    hours = raw_input('Enter Hours: ')
    hours = float(hours)
    rate = raw_input('Enter Rate: ')
    rate = float(rate)
except:
    print 'Error, please enter numeric input'

overtime = hours % 40

if hours > 40:
    pay = (40 * rate) + (overtime * rate * 1.5)
else:
    pay = hours * rate

print 'Pay:', pay