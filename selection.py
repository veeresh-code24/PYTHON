def selection_sort(nums):
    for i in range(len(nums)):
        mini=i
        for j in range(i+1,len(nums)):

            if nums[j]< nums[mini]:
                mini=j
        
        nums[i],nums[mini]=nums[mini],nums[i]

    return nums



n=int(input("enter the number of element do u want to insert:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"enter the {i}th element")))


print("elements before sorting:",arr)

print(selection_sort(arr))

