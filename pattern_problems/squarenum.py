# Write a program to draw this pattern

'''
1 2 3 4
1 2 3 4
1 2 3 4

'''
n = 4

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j, end=" ")

    print()