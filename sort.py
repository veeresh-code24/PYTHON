def max_consec(nums):
    maxi = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            if count > maxi:
                maxi = count

        else:
            count = 0
    return maxi

nums = [1,1,0,1,1,1]
print(max_consec(nums))