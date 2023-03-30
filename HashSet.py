# Time Complexity :
#  Space Complexity :
#  Did this code successfully run on Leetcode :
#  Any problem you faced while coding this :

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.bucketSize = 1001
        self.array = [None for i in range(self.buckets)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        # O(1) Time Complexity | O(1) Space Complexity
        bucketRowIndex = key % self.buckets
        bucketColIndex = int(key / self.bucketSize)
        if self.array[bucketRowIndex] == None:
            self.array[bucketRowIndex] = [
                False for i in range(self.bucketSize)]
        self.array[bucketRowIndex][bucketColIndex] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # O(1) Time Complexity | O(1) Space Complexity
        bucketRowIndex = key % self.buckets
        bucketColIndex = int(key / self.bucketSize)
        if self.array[bucketRowIndex] != None:
            self.array[bucketRowIndex][bucketColIndex] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        # O(1) Time Complexity | O(1) Space Complexity
        bucketRowIndex = key % self.buckets
        bucketColIndex = int(key / self.bucketSize)
        return self.array[bucketRowIndex] != None and self.array[bucketRowIndex][bucketColIndex] == True
