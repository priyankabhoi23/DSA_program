# Find the minimum and maximum element from unsorted array... Without using sort, min, max function

arr=list(map(int,input().split()))
mini=arr[0]
maxi=arr[0]
for i in arr:
    if i < mini:
        mini=i
    if i > maxi:
        maxi=i
print("Min=",mini,"Max= ", maxi)

        
