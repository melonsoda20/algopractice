from typing import List


def max_area(height: List[int]) -> int:
    if len(height) < 2:
        return 0

    left_pointer_index = 0
    right_pointer_index = len(height) - 1
    max_area_value = 0

    while(left_pointer_index < right_pointer_index):
        min_value = height[left_pointer_index]
        if(height[right_pointer_index] < min_value):
            min_value = height[right_pointer_index]
        index_distance = right_pointer_index - left_pointer_index
        cur_area_value = min_value * index_distance
        if cur_area_value > max_area_value:
            max_area_value = cur_area_value

        if min_value is height[left_pointer_index]:
            left_pointer_index += 1
        else:
            right_pointer_index -= 1

    return max_area_value


height_data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area_result = max_area(height_data)

print(max_area_result)
