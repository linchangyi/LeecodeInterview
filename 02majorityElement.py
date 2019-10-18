'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''
from typing import List


# 排序，中间的即为众数
def majorityElement(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


# 摩尔投票法
def majorityElement2(nums: List[int]) -> int:
    m, c = nums[0], 0
    for num in nums:
        if c == 0:
            c += 1
            m = num
        elif num == m:
            c += 1
        else:
            c -= 1
    return m


if __name__ == '__main__':
    print(majorityElement([1, 2, 2]))
    print(majorityElement2([1, 2, 2]))
