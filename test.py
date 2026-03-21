# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         min_value = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_value]:
#                 min_value = j

#         arr[i],arr[min_value] = arr[min_value],arr[i]
#         print(*arr)


# arr = [4,3,1,7,2]
# selection_sort(arr)
# print(arr)

def bubble_sort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]

    print(*arr)
arr = [1,8,3,2,5]
n = 5
bubble_sort(arr,n)
