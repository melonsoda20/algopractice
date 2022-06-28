from typing import List


class Solution:
    def findKthLargest(nums: List[int], k: int) -> int:
        index_to_find = len(nums) - k
        Solution.quickSort(nums, 0, len(nums) - 1)
        return nums[index_to_find]

    def swap(nums: List[int], first_index: int, last_index: int):
        temp_value = nums[first_index]
        nums[first_index] = nums[last_index]
        nums[last_index] = temp_value

    def partition(nums: List[int], left_index: int, right_index: int):
        pivot_element = nums[right_index]
        partition_index = left_index
        while(left_index < right_index):
            if nums[left_index] < pivot_element:
                Solution.swap(nums, partition_index, left_index)
                partition_index += 1
            left_index += 1
        Solution.swap(nums, partition_index, right_index)
        return partition_index

    def quickSort(nums: List[int], left_index: int, right_index: int):
        if left_index < right_index:
            partition_index = Solution.partition(nums, left_index, right_index)
            Solution.quickSort(nums, left_index, partition_index - 1)
            Solution.quickSort(nums, partition_index + 1, right_index)


print(Solution.findKthLargest([5, 3, 1, 6, 4, 2], 2))
