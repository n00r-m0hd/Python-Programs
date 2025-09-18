nterms = int(input("Enter nth term of Fibonacci Sequence"))

n1 , n2 = 0, 1

count = 0

if nterms < 0:
    print("Please enter a valid or a positive number")

elif nterms == 0:

    print("Please enter a positive number")

else:
    while count < nterms:
        print(n1)

        nth = n1 + n2

        n1 = n2

        n2 = nth

        count = count + 1

