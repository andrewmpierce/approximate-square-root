import sys

x = input("What's your number? Must be positive.")
#if x == str(x): sys.exit("Thats not a valid response.")
#if x <= 0: sys.exit("That's not a valid response.")

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
