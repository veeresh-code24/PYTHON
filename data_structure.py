# Linear search

'''def liner_search(a,key):
    for i in range(0, len(a)):
        if a[i] == key:
            return i
    
    return -1

a = [10,20,30,40,55]
key = 90
print(liner_search(a,key))'''

# Span_array

'''def span_list(n):
    max = n[0]
    min = n[0]

    for i in range(0, len(n)):
        if n[i] > max:
            max = n[i]

        if n[i] < min:
            min = n[i]

    return max - min

n = [12,21,32,43,56,78,98,99,102]
print(span_list(n))'''
        
# largest element

'''def lar_array(a):
    largest = a[0]

    for i in range(0 ,len(a)):
        if a[i] > largest:
            largest = largest

    return largest

a = [12,21,3,26,7,8,122]
print(lar_array(a))'''

# second largest number

'''def sec_largest(a):
    max1,max2=0,0

    if a[0] > a[1]:
        max1,max2 = a[0],a[1]
    else:
        max1,max2 = a[1],a[0]

    for i in range(2, len(a)):
        if a[i] > max1:
            max2 = max1
            max1 = a[i]

        elif a[i] > max2:
            max2 = a[i]

    return max2,max1

a = [12,21,87,23,43,56,78,89,110,1002]
print(sec_largest(a))'''

# Biary search

'''def binary_ser(a,key):
    l,h,mid = 0, len(a)-1, 0
    while l <= mid:
        mid = l+h//2
        if key == a[mid]:
            return a[mid]
        
        elif key <= mid:
            h = mid -1
            l = l

        else:
            l = mid +1
            h = h
    return -1

a = [12,21,23,31,34,31,21]
key = 334
print(binary_ser(a,key))'''

# def ascending_ord(a, key):
#     l, h,m= 0, len(a)-1, 0

#     while l <= h:

#         m = (l+h)//2
#         if key == a[m]:
#             return m
#         elif key < a[m]:
#             h = m -1

#         else:
#             l = m +1

#     return -1

# a= [12,21,21,21,23,23,43]
# key = 99
# print(ascending_ord(a, key))

# def count_lesser(a,key):
#     l,h,mid = 0 ,len(a)-1, 0

#     while l <= h:
#         mid = (l+h)//2

#         if key == a[mid]:
#             return mid +1
        
#         elif key < mid:
#             h = mid-1

#         else:
#             l = mid +1

#     while mid+1 < len(a) and key == a[mid+1]:
#         mid +1

#         return mid

# a = [2,6,12,18,21,26,33,42]
# key = 21

# print(count_lesser(a,key))


# smaller and wqual count

'''def small_count(a,key):
    l,h = 0, len(a)
    ans = 0

    while  l <= h:
        mid = (l+h)//2
        if a[mid] <= key:
            ans = mid+1
            l = mid+1

        else:
            h = mid-1

    return ans

a = [2,3,12,24,28,36]
key = 26

print(small_count(a,key))'''

# sorted array

'''def sorted_ar(a):
    return all(a[i] >= a[i-1] for i in range(1,len(a)))

    for i in range(1,len(ar)):
        if ar[i] > ar[i-1]:
            return True
        
    return False

a = [1,2,4,6,8,10,12]
print(sorted_ar(a))'''

# Reverse Array

'''def main(a):

    i,j = 0,len(a)-1

    while i < j:
        t = a[i]
        a[i] = a[j]
        a[j] = t
        i += 1
        j -= 1

a = [2,3,4,56,7,8,910]
print(a)
main(a)
print(a)'''

# Inverse Array

# def inverse_arr(ar):
#     b = [0] * len(ar)

#     for i in range(0,len(ar)):
#         v = ar[i]
#         b[v] = i

#     return b

# ar = [2,3,1,0,4]
# print(inverse_arr(ar))


# find the first and last index position if number is same 

'''def searchrange(nums,target):
    l,h,mid = 0,len(nums)-1,0
    res = [-1,-1]

    while l <= h:
        mid = (l+h)//2

        if target == nums[mid]:
            res[0] = mid
            h = mid-1

        elif target < nums[mid]:
            h = mid - 1

        else:
            l = mid+1
    
    l,h,mid = 0,len(nums)-1,0

    while l <= h:
        mid = (l+h)//2

        if target == nums[mid]:
            res[1] = mid
            l = mid+1

        elif nums[mid] < target:
             h = mid - 1


        else:
            l = mid+1

    return res

nums = [3,4,4,4,4,4,4,4,6]
target = 4

print(searchrange(nums,target))'''

# Search rotated sorted arry

'''def sorted_array(a,target):
    l,h,mid = 0, len(a)-1, 0

    while l <= h:
        mid = (l+h)//2
        if target == a[mid]:
            return mid
        # left side sorted
        if a[l] <= a[mid]:
            if a[l] <= target < a[mid]:
                h = mid -1
            else:
                l = mid +1

        else:
            if a[mid] < target <= a[h]:
                l = mid+1
            else:
                h = mid -1

    return -1


a = [7,8,1,2,4,5,6]
target = 1
print(sorted_array(a,target))'''


def sorted_arrar(a,target):
    l,h,mid = 0, len(a)-1,0

    while l <= h:
        mid = (l+h)//2
        if target == a[mid]:
            return mid
        
        if a[l] <= a[mid]:
            if a[l] <= target < a[mid]:
                h = mid -1
            else:
                l = mid +1

        else:
            if a[mid] < target <= a[h]:
                l = mid+1
            else:
                h = mid-1

    return -1
 

a = [7,8,1,2,4,5,6]
target = 4
print(sorted_arrar(a,target))