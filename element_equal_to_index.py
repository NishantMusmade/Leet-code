# The array is in increasing order, find an element 'i' such that arr[i] = i

def find_element(a,n):
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2
        if a[mid] == mid:
            return mid
        elif mid > a[mid]:
            low = mid + 1
        else:
            high = mid-1
        
    return -1


arr = [-2,-1,0,1,2,5,8,10,90]

index = find_element(arr,len(arr))

if index == -1:
    print("Element not found...!")
else:
    print(f"Element found at index {index}")


# If the array is non-decreasing that means elements are repeating, then binary search will not work