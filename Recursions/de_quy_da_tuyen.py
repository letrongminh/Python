def print_arr(arr):
    print(arr)

def print_per(arr, n):
    print_arr(arr)
    for i in range (0, n):
        for j in range (0, n):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            j+=1
        i+=1
        print(arr)
M=[3, 9, 6]
test2 = print_per(M, len(M))
print(test2)
