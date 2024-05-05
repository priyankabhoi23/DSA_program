arr=list(map(int,input().split()))
n=int(input("Enter the no of count to search:"))
count=0
for i in arr:
    if n==i:
        count=count+1
print(count)
        
    