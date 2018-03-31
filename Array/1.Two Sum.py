#Array | Hash Table
#给一个整数数组，找到两个数使得他们的和等于一个给定的数target
#example
#Given nums = [2, 7, 11, 15], target = 9
#Because nums[0] + nums[1] = 2 + 7 = 9
#return [0, 1]

#自己
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                j=nums.index(target-nums[i])
                if i!=j:     #通过索引判断是否重复
                    return [i,j]
                    
#其他                 
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}  #hash table
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            dic[target - num] = index

#错误点：没有判断如果list中有重复的情况

#思路： Ⅰ遍历+索引([].index())； Ⅱ索引和值可以考虑到hash表+key和value结构；让key就是要找的b，让value记录a的index，也就是结果需要的索引(他人)
