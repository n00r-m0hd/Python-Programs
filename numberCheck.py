# n=int(input("Enter your value:"))

# start=1
# end=100

# if start<=n<=end:
#     print(f"{n} is present")


# else:
#     print(f"{n} is not present in the given range")

# Another logic for this progrm

n=int(input("Enter your number\n"))

found=False

for i in range(1,101):
    if i==n:
        found=True
        break


if found:
    print(f"{n} is present in the given range")

else:
    print(f"{n} is not present in the given range")