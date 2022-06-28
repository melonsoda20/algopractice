from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstPositionOfTarget = self.getFirstPositionTarget(nums, target)
        lastPositionOfTarget = self.getLastPositionTarget(nums, target)

        return[firstPositionOfTarget, lastPositionOfTarget]

    def getFirstPositionTarget(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        # Find the first occurence of the target
        while(left_pointer <= right_pointer):
            mid_index = (left_pointer + right_pointer) // 2
            if(nums[mid_index] == target):
                # Check if this is the first time
                # that the target appears on the array
                if(mid_index == 0 or (
                    mid_index - 1 >= 0 and
                    nums[mid_index-1] != target
                )):
                    return mid_index
                else:
                    right_pointer = mid_index-1
            elif(nums[mid_index] > target):
                right_pointer = mid_index - 1
            else:
                left_pointer = mid_index + 1
        return -1

    def getLastPositionTarget(self, nums, target):
        left_pointer = 0
        right_pointer = len(nums) - 1
        # Find the last occurence of the target
        while(left_pointer <= right_pointer):
            mid_index = (left_pointer + right_pointer) // 2
            if(nums[mid_index] == target):
                # Check if this is the first time that
                # the target appears on the array
                if(mid_index == len(nums)-1 or (
                    mid_index+1 < len(nums) and nums[mid_index+1] != target
                )):
                    return mid_index
                else:
                    left_pointer = mid_index+1
            elif(nums[mid_index] > target):
                right_pointer = mid_index - 1
            else:
                left_pointer = mid_index + 1
        return -1
