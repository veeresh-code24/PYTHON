# def max_consec(nums):
#     maxi = 0
#     count = 0

#     for i in range(len(nums)):
#         if nums[i] == 1:
#             count += 1
#             if count > maxi:
#                 maxi = count

#         else:
#             count = 0
#     return maxi

# nums = [1,1,0,1,1,1]
# print(max_consec(nums))

# def single(nums):

#     for i in range(len(nums)):
#         num = nums[i]
#         count = 0

#         for j in range(len(nums)):
#             if nums[j] == num:
#                 count += 1

#         if count == 1:
#             return num



# nums = [1, 2, 2, 4, 3, 1, 4]
# print(single(nums))

def sub_array(nums):

    for i in range(len(nums)):
        su = 0
        for j in range(i, len(nums)):
            su = nums[j] + su
            su = su == key
            print(su)
   
            print(nums[i:j+1])
key = 15
nums = [1, 2, 2, 4, 3, 1, 4]
sub_array(nums)

