# def largest(arr):
#     return arr[-1]

    
# arr = [3,2,1,15,2]
# arr.sort()
# print(largest(arr))


# def largest_element(arr):
#     n = len(arr)
#     largest = arr[0]

#     for i in range(1,n):
#         if arr[i] > largest:
#             largest = arr[i]

#     return largest

# arr = [3,2,1,15,2]
# print(largest_element(arr))


# def second_largest(arr):
#     largest = arr[-1]

#     for i in range(n-1,-1,-1):
#         if arr[i] != largest:
#             return arr[i]

# arr = [1,2,15,7,7]
# n = 5
# arr.sort()
# print(second_largest(arr))


def fir_largest(arr,n):
    fir_largest = arr[0]
    second_largest = float('inf')

    for i in range(1,n):
        if arr[i] < fir_largest:
            second_largest = fir_largest
            fir_largest = arr[i]

        elif arr[i] > second_largest and arr[i] < fir_largest:
            second_largest = arr[i]

    return second_largest


    # for i in range(1,n):
    #     if arr[i] > fir_largest:
    #         fir_largest = arr[i]

    # second_largest = -1

    # for i in range(n):
    #     if arr[i] > second_largest and arr[i] != fir_largest:
    #         second_largest = arr[i]

    # return second_largest,fir_largest

arr = [3,2,110,500,7,6]
n = 6
print(fir_largest(arr,n))
