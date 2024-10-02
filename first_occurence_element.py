# The array is in non decreasing order, find the first occurence of the given element 


def first_occurence(a,n,x):
    low = 0
    high =  n-1

    while low<=high:
        mid = (low+high)//2
        if x == a[mid]:
            if low == high or x > a[mid-1]:
                return mid
            else:
                high = mid - 1
        elif x > a[mid]:
            low = mid+1
        else:
            high = mid-1
    
    return -1



arr = [1,2,2,3,3,3,4,4,4,5,6,7,8,8,9]
x = 1
index = first_occurence(arr,len(arr),x)

if index == -1:
    print("Element not found...!")
else:
    print(f"Element's first occurence is at index {index}")