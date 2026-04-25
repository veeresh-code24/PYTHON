# def count_subarray(nums,k):
#     n = len(nums)
#     count = 0 

#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += nums[j]

#             if sum == k:
#                 count += 1

#     return count

# nums = [1,2,3]
# k = 2
# print(count_subarray(nums,k))


def longest_subarray(nums,k):
    n = len(nums)
    d = {}
    max_len = 0
    sum = 0

    for i in range(n):
        sum += nums[i]

        if sum == k:
            max_len = max(max_len,i+1)

        lens = sum-k
        if lens in d:
            ab = i-d[lens]
            max_len = max(max_len,ab)

        if  sum not in d:
            d[sum] = i



    return max_len


nums = [-1,-2,3,1,1,1]
k = 3
print(longest_subarray(nums,k))




