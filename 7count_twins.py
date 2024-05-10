li=list(map(int,input().split()))
count = 0
for i in range(len(li) - 1):
    if li[i] == li[i + 1]:
      count += 1
print(count)


    
        