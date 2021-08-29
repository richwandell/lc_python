import bisect


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.compliments = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        bisect.insort(self.nums, number)
        self.compliments = {}

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if value not in self.compliments:
            self.compliments[value] = {}
        for x in self.nums:
            if value - x in self.compliments[value]:
                return True
            else:
                self.compliments[value][x] = x
        return False


obj = TwoSum()
obj.add(1)
obj.add(3)
obj.add(5)
print(obj.find(4))
print(obj.find(7))
