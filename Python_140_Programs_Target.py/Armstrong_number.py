#Write a python program to check whether a given number is Armstrong or not

# 153 = 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153

num = int(input("Enter a number\n"))

num_str = str(num)

num_digits = len(num_str)

sum_of_powers = 0

temp_num = num


while temp_num > 0:

    digits = temp_num % 10
    sum_of_powers = sum_of_powers + digits ** num_digits
    temp_num = temp_num//10

if sum_of_powers == num:
    print(f"{num} is an Armstrong number")

else:
    print(f"{num} is not an Armstrong number")