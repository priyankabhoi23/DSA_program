n,x=map(int,input("Enter elements to search").split())
arr=list(map(int,input("Enter array element:").split()))
if n in arr and x in arr:
    print("Yes")
else:
    print("No")
