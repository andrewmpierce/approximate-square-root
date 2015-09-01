import sys

x = int(input("What's your number? Must be positive."))
if not x >= 1: sys.exit("That's not a valid response.")

x = int(x)
def sqrt():
    y = 1
    counter = 0
    while round((y*y - x),2) != 0:
        y = (y + (x/y))/2
        counter += 1
        print("This is round {}".format(counter))
        #print(y) Used to test while loop
    return print(y)
sqrt()
