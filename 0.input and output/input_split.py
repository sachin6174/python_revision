txt = input();
k=int(input());

x = txt.split()
arr=[]
for e in x :
    arr.append(int(e))

sum=0
for e in arr :
    sum+=e

print(type( arr),arr ,sum,k)