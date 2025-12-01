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



def insertion_sort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j > 0 and key < nums[j]:
            nums[j+1]= nums[j]

        

        nums[j+1]=key
    

    return nums



nums=[1,0,1,4,5,3,0]
print(insertion_sort(nums))



