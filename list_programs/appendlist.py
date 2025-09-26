numbers = []

n = int(input("Enter how many numbers do you want enter in the list!\n"))

for i in range(1,n+1):
    num = int(input())
    numbers.append(num)

print("You entered these numbers in list")
print(numbers)

print("Reversed list: ")

print(numbers[::-1])