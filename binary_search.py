def binary(a,t):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==t:
            return mid
        elif a[mid]<t:
            low=mid+1
        else:
            high=mid-1
    return -1
n=[1,2,3,4,5,6,7]
t=7
i=binary(n,t)
print(f"found at {i}")
