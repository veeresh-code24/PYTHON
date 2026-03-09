# Linear search

def liner_search(a,key):
    for i in range(0, len(a)):
        if a[i] == key:
            return i
    
    return -1

a = [10,20,30,40,55]
key = 90
print(liner_search(a,key))
        
