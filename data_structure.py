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

def binary_ser(a,key):
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
print(binary_ser(a,key))

    
    


