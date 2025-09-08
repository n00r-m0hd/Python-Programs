def avg_num(a,b,c):
    sum = a + b + c

    avg = sum/3

    return avg

a1 = float(input("Enter first number\n"))
a2 = float(input("Enter second number\n"))
a3 = float(input("Enter third number\n"))

avg = avg_num(a1,a2,a3)

print(f"Average of {a1} , {a2} , and {a3} is {avg}")