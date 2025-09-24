y = input("Enter a guest")
a = input("Enter a number")
b = input("Enter another number")


c = input("Will you be multiplying?")
d = input("Will you be dividing?")
e = input("Will you be subtracting")

f = input("Will you be adding")



if f == "Yes":

    n = input("you will be adding the two numbers, proceed?")
    if n == "Yes":

        o = a + b

        print(y, "'s result is:")
        print(o)
if e == "Yes":
    n = input("you will be adding the two numbers, proceed?")
    if n == "Yes":
        i = a - b
        print(y, "'s result is:")

        print(i)
if d == "Yes":
    n = input("you will be multiplying the two numbers, proceed?")
    if n == "Yes":

        f = a * b


        print(y,"'s result is:")
        print(f)
if c == "Yes":
    n = input("you will be dividing the two numbers, proceed?")
    if n == "Yes":

        print(y, "'s result is:")
        g = b / a

        print(g)





