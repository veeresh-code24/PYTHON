def insertion_sort(nums):
    for i in range(len(nums)):

        key=i+1
        j=i

        while j >=0  and nums[j]<=nums[key]:
            if nums[j]<nums[key]:
               nums[key],nums[j]=nums[j],nums[key]
    

            j-=1
    
    return nums



nums=[2,41,171,39,0]
print(insertion_sort(nums))