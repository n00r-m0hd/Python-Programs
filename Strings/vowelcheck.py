my_str = "Python programming has written by Guido Van Rosum"

vowels = 'aeiou'

count = 0

for x in my_str:
    if x.lower() in vowels:
        count = count+1

print(f"Numbers of vowels {count}")