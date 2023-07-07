def linear(a,t):
    for i in range(len(a)):
        if a[i]==t:
            return i
    return -1
n=[5,9,2,7,1,8,3]
t=7
index=linear(n,t)
print(f"target found at:{index}")
    
    
