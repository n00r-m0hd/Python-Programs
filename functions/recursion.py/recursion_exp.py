def facto_rial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * facto_rial(n-1)
        

f = facto_rial(5)

print(f"Facorial is {f}")