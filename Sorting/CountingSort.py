def countingSort(mylist, high):
    counter = [0] * (high+1)
    for i in mylist:
        counter[i] += 1

    startpoint = 0
    for i in range(len(counter)):
        while 0 < counter[i]:
            mylist[startpoint] = i
            startpoint += 1
            counter[i] -= 1


arr = [5,3,2,3,6,1]
countingSort(arr,max(arr))
print(arr)