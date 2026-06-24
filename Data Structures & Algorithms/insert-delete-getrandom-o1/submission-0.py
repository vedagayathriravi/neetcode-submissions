#we are using hashmap and arrays for this problem.Because hashmap is to add and remove the elements and for the randomized elements we need to use array as we cant do it in the hashset.Why we are not doing in the hashset is that when removing the element in array while doing the remove operation,it will be not possible to remove randomly so for that case we are using hashmap where it can redirect the indexes. And also when removing the element in the array,we cant keep it empty or put the same number that already exists,so what we are doing is that we are moving the last index value to the empty index and changing the redirecting value in the hashmap.
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.numMap[last] = idx
        self.nums.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()