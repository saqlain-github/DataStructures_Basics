#FIFO
#mcdonalds

#bad approach

myqueue = []
myqueue.append("superman")
myqueue.append("batman")
myqueue.append("aquaman")
myqueue.pop(0) #after deletion all elements are rearranged so bad approach

#better approach 2

from collections import deque

myq = deque()
myq.append("batman")
myq.append("superman")
myq.append("flash")
print(myq)
myq.popleft() #less expensive
print(myq)


#better approach 2

from queue import Queue

myque = Queue()
myque.put("superman")
myque.put("aqueman")
myque.put("flash")

print(myque)
myque.get()
myque.get()
myque.get()
myque.get() #use .get_nowwait()