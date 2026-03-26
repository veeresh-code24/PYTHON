def sub_array(nums,k):
    n = len(nums)
    right = 0
    left = 0
    sum = nums[0]
    max_sum = 0

    while right < n:
        while left <= right and sum > k:
            sum -= nums[left]
            left += 1

        if sum == k:
            max_sum = max(max_sum,right-left+1)
        
        right += 1
        if right < n :
            sum += nums[right]

    return max_sum

nums = [1,2,3,1,1,1,1,4,2,3]
k = 3
print(sub_array(nums,k))