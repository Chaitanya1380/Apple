a=8
c=0
for i in range(2,a):
    if(a%i==0):
        c=c+1
if(c==0):
    print("prime")
else:
    print("not prime")
