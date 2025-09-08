# def facto(n):
#     f = 1 
#     i = 1
#     while(i<=n):
#         f = f * i

#         i = i + 1
#     return f
# f1 = facto(5)

# print(f1)

def facto(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
        
    return f

# f1 = facto(5)

# print(f1)
print(facto(5))