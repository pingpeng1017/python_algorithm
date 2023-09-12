n = []
for i in range(6):
    n.append(int(input()))
    
arr1 = sorted(n[:4])
arr2 = n[4:]
print(sum(arr1[1:]) + max(arr2))