
#TODO: Helper - partiton, helper

def helper(arr,low, high):
    pivot_index = arr[high]
    i = low - 1

    #crossed i and j
    for j in range(low,high):
        if arr[j] <= pivot_index:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

#TODO: sort

def quicksort(arr,low,high):
    if low < high:
        piv = helper(arr,low,high)
        quicksort(arr,low,piv-1)
        quicksort(arr,piv+1,high)


#TODO: test the code

arr = [5,7,8,6,8,1,0,3]

quicksort(arr,0,len(arr)-1)
print(arr)
