#cs.usfca.edu

#self.rear+1 % self.size == self.front (full)

class CircularQueue:
    def  __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.front.rear = -1

    def enqueue(self,data):
        if (self.rear+1) % self.size == self.front :
            print("queue is full")
            return
        elif (self.front == -1):
            self.front =0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print("queue is empty")
            return
        elif (self.front == self.rear):
            popval = self.queue[self.front]
            self.front = -1
            self.rear = -1
        else:
            popval = self.queue[self.front]
            self.front = (self.front +1) % self.size

        return popval
