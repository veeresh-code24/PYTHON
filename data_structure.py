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
        
# Second largest element

def lar_array(a):
    largest = a[0]

    for i in range(0 ,len(a)):
        if a[i] > largest:
            largest = largest

    return largest

a = [12,21,3,26,7,8,122]
print(lar_array(a))