'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109

Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_element = 0

        for element in nums:
            for other_element in nums[index_element + 1:len(nums)]:
                if element + other_element == target:
                    answer = [element, other_element]
                    break
            index_element = index_element + 1

        if answer[0] == answer[1]:
            index_answer = []
            for index in range(len(nums)):
                if nums[index] == answer[0]:
                    index_answer.append(index)
        else:
            index_answer = [nums.index(answer[0]), nums.index(answer[1])]

        return index_answer