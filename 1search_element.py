arr=list(map(int,input("Enter array element:").split()))
n,x=map(int,input("Enter elements to search").split())
if n in arr and x in arr:
    print("elements found")
else:
    print("elements not found")