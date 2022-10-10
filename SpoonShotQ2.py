def solver(arr):
    output = [1] * len(arr)

    left_product = 1
    for i in range(1, len(arr)):
        left_product *= arr[i-1]
        output[i] = left_product

    right_product = 1
    for i in range(len(arr)-2, -1, -1):
        right_product *= arr[i+1]
        output[i] *= right_product
    
    return output

arr = list(map(int,input().split()))
print(solver(arr))
