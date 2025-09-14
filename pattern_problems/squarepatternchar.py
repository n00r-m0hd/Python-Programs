'''
Write a python program to draw this pattern

A B C D
A B C D
A B C D
A B C D
'''


n = 4

for i in range(n):
    # ch = 'A'
    for j in range(n):
        # print(ch, end = " ")

        print(chr(ord('A') + j), end=" ")
        
        """
        You're trying to increment a character, but in Python, 
        you can't directly increment a string like that.
        You need to use the ord() and chr() functions to manipulate characters by their ASCII values.
        ch = ch + 1
        """
       

    print()