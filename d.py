# MORE EFFICIENT CODE
# run program that prints numbers 1-100
# multiples of 3 print fizz
# mulitples of 5 print buzz
# mulitples of 3 & 5 print fizzbuzz
for n in range(1,101):
    if (n % 3 == 0 and n % 5 == 0):
        print("fizzbuzz")
    elif (n % 3 == 0):
        print("fizz")
    elif (n % 5 == 0):
        print("buzz")
    else:
        print(n)
