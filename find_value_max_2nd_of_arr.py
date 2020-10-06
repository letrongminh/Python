import array
max1 = 0
max2 = 0
arr = []
n = int(input("element's number of array: "))
for a in range(n):
    arr.append(int(input("type element %d =" % (a+1) )))
print(arr)    
for i in range(n+1):
    if i==n:
        for j in range(n):
            if j == n-1:
                print("Max 2nd of array: ", max2)
            else:
                if max1 > arr[j]:
                    if max2 < arr[j]:
                        max2=arr[j]
                    else:
                        j += 1
                else:
                    j += 1
    else:
        if max1 < arr[i]:
            max1 = arr[i]
            i+=1
        else:
            i += 1
