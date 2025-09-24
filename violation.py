y = input("Enter a guest")
a = input("Enter a number")
b = input("Enter another number")


c = input("Will you be multiplying?")
d = input("Will you be dividing?")
e = input("Will you be subtracting")

f = input("Will you be adding")



if f == "Yes":

    n = input("you will be adding the two numbers, proceed?")
    if n == "yes":

        o = int(a) + int(b)

        print(y, "'s result is:")
        print(o)
if e == "Yes":
    n = input("you will be adding the two numbers, proceed?")
    if n == "yes":
        i = int(a) - int(b)
        print(y, "'s result is:")

        print(i)
if d == "Yes":
    n = input("you will be multiplying the two numbers, proceed?")
    if n == "yes":

        f = int(a) * int(b)


        print(y,"'s result is:")
        print(f)
if c == "Yes":
    n = input("you will be dividing the two numbers, proceed?")
    if n == "yes":

        print(y, "'s result is:")
        g = int(b) / int(a)

        print(g)





