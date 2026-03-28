# def bubble_sort(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
            
        
    
#     return nums



# nums=[1,0,8,4,5,3,0]
# print(bubble_sort(nums))




# def selection_sort(nums):
#     n = len(nums)

#     count0 ,count1,count2 = 0,0,0
#     for i in range(n):
#         if nums[i] == 0:
#             count0 += 1
#         elif nums[i] == 1:
#             count1 += 1
#         else:
#             count2 += 1
#     i = 0
#     while i < count0:
#         nums[i] = 0
#         i +=1

#     while i < count0+count1:
#         nums[i] = 1
#         i+=1

#     while i < n:
#         nums[i] = 2
#         i+=1

#     return nums

# nums= [1,0,2,1,0,0,1,1,2,1,0]
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
# print("100")

# def majority_ele(nums):
#     n = len(nums)
#     d = {}

#     for i in nums:
#         if i not in d:
#             d[i] = 1

#         else:
#             d[i] += 1

#     for key,value in d.items():
#         if value > n//2:
#             return key
        
#     return -1

# nums = [3,2,3,3,2,2,3,3,3,3,2,2,2,2,2,2,2]

# print(majority_ele(nums))



# def majority_element(nums):
#     cnt = 0
#     el = None

#     # Step 1: Find candidate
#     for num in nums:
#         if cnt == 0:
#             cnt = 1
#             el = num
#         elif num == el:
#             cnt += 1
#         else:
#             cnt -= 1

#     # Step 2: Verify candidate
#     cnt1 = 0
#     for num in nums:
#         if num == el:
#             cnt1 += 1

#     if cnt1 > len(nums) // 2:
#         return el

#     return -1


def maxi(nums):
    n = len(nums)
    max_sum = 0


    for i in range(n):

        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]

                max_sum = max(max_sum,sum)


    return max_sum
      
nums = [5,4,-1,7,8]
print(maxi(nums))



                

