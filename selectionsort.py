def selection(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a
b=[2,3,1,4]
s=selection(b)
print(s)
    
