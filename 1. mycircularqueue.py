# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
# Your implementation should support following operations:
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.
class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size= k
        self.myqueue = []
        
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull() == True:
            return False
        else:
            self.myqueue.append(value)
            return True
            
            
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() == True:
            return False
        else:
            self.myqueue.pop(0)
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty() == True:
            return -1
        else:
            return self.myqueue[0]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty() == True:
            return -1
        else:
            rear = self.myqueue[len(self.myqueue) -1]
        return rear

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if len(self.myqueue) == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if len(self.myqueue) == self.size:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()