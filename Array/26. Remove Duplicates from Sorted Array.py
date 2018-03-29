#题意：给定一个排好序的数组，去除重复的数，返回新数组的长度(不能申请额外的空间，超过新数组长度部分是什么数都无所谓),即不能新建数组


##自己存在的问题：没有考虑list变化后index也在变，[list index out of range];未注意已经排好序

#思路：使用一个指针j，当i向后遍历数组时，如果遇到与A[j]不同的，将A[i]和A[j+1]交换，同时j=j+1，即j向后移动一个位置，然后i继续向后遍历。

#总结：指针用法？空list
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1
        
       
# https://blog.csdn.net/guoziqing506/article/details/51395796
#就是碰到需要删除元素的数组，进行遍历时，尽量用while循环，通过下标和变动数组长度的关系来控制循环结束的条件
