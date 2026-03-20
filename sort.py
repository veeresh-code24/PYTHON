# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
            
        
    
#     return nums



# nums=[1,0,8,4,5,3,0]
# print(bubble_sort(nums))




# def selection_sort(nums):
#     for i in range(len(nums)):
#         mini=i
#         for j in range(i+1,len(nums)):
#             if nums[j]<nums[mini]:
#                 mini=j
            
#         nums[i],nums[mini]=nums[mini],nums[i]
    

#     return nums



# nums=[1,0,1,4,5,3,0]
# print(selection_sort(nums))



# def insertion_sort(nums):
#     for i in range(1,len(nums)):
#         key=nums[i]
#         j=i-1
#         while j > 0 and key < nums[j]:
#             nums[j+1]= nums[j]

        

#         nums[j+1]=key
    

#     return nums



# nums=[1,0,1,4,5,3,0]
# print(insertion_sort(nums))


# bubble sort

'''def bubble_sort(arr,n):
    for i in range(n):
        did_swap = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # arr[j],arr[j+1] = arr[j+1],arr[j]
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

                did_swap = 1

        if did_swap == 0:
            break
        print("didn't run")

        
    print(*arr)

arr = [2,3,4,5,6]
n = 5
bubble_sort(arr,n)'''

# insertion sort
'''def insertion_sort(arr,n):

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >=0 and arr[j] > key:
             arr[j+1] = arr[j]
             j -= 1

        arr[j+1] = key
    return arr

arr = [3,5,8]
n = 3
print(insertion_sort(arr,n))'''

# def bubble_sort(arr,n):
#     for i in range(n-1,-1,-1):
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]

#     print(*arr)

# arr = [1,2,64,54,23]
# n = 5
# bubble_sort(arr,n)


def insertion_sort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    print(*arr)

arr = [2,1,34,53,12,1]
n = 6
insertion_sort(arr,n)

 
















