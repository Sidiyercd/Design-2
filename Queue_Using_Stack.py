# Time Complexity :
#  Space Complexity :
#  Did this code successfully run on Leetcode :
#  Any problem you faced while coding this :
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # O(1) Time Complexity | O(1) Space Complexity
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # O(1) Time Complexity (best and average)| O(n) Time Complexity (worst)
        # O(n) Space Complexity
        if (len(self.stack2) == 0):
            self.transfer()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # O(1) Time Complexity (best and average)| O(n) Time Complexity (worst)
        # O(n) Space Complexity
        if (len(self.stack2) == 0):
            self.transfer()
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        # O(1) Time Complexity | O(1) Space Complexity
        return (len(self.stack1) == 0 and len(self.stack2) == 0)

    def transfer(self):
        '''
        Push elements from stack 1 to stack 2
        :rtype: None
        '''
        while (len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())
