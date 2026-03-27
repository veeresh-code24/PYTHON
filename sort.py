# def sub_array(nums,k):
#     n = len(nums)
#     right = 0
#     left = 0
#     sum = nums[0]
#     max_sum = 0

#     while right < n:
#         while left <= right and sum > k:
#             sum -= nums[left]
#             left += 1

#         if sum == k:
#             max_sum = max(max_sum,right-left+1)
        
#         right += 1
#         if right < n :
#             sum += nums[right]

#     return max_sum

# nums = [1,2,3,1,1,1,1,4,2,3]
# k = 3
# print(sub_array(nums,k))


# def rotate_arr(nums,k):
#     n = len(nums)
#     temp = nums[0:k]

#     for i in range(k,n):
#         nums[i-k] = nums[i]
#     x = 0
#     for h in range(n-k,n):
#         nums[h] = temp[h-(n-k)]
#         x += 1

#     return nums

# def rotate_array(nums,k):
#     n = len(nums)
#     k = k%n

#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
#     nums[:] = reversed(nums)



#     return nums



# nums = [1,2,3,4,5,6]
# k = 3
# print(rotate_array(nums,k))

# def two_sum(nums,target):
#     n = len(nums)

#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                 return i,j
            

# nums = [2,6,5,8,11]
# target = 14
# print(two_sum(nums,target))


def two_sum(nums,target):
    n = len(nums)
    left = 0

    right = n-1

    while left < right:
        sum_arr = nums[left] + nums[right]
        if sum_arr == target:
            return "Yes"
        
        elif sum_arr < target:
            left += 1
        else:
            right -=1

    return "No"
        


nums = [2,5,6,8,11]
target = 14
print(two_sum(nums,target))
        
    


