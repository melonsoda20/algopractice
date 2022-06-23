from typing import List


def trap_brute_force(height: List[int]) -> int:
    if len(height) < 3:
        return 0

    water_count = 0
    height_len = len(height)

    for index, value in enumerate(height):
        max_left_pointer_value = 0
        max_right_pointer_value = 0
        left_pointer_index = index
        right_pointer_index = index

        while left_pointer_index > -1:
            max_left_pointer_value = max(
                max_left_pointer_value,
                height[left_pointer_index]
            )
            left_pointer_index -= 1

        while right_pointer_index < height_len:
            max_right_pointer_value = max(
                max_right_pointer_value,
                height[right_pointer_index]
            )
            right_pointer_index += 1

        min_height_value = min(max_left_pointer_value, max_right_pointer_value)
        calc_result = min_height_value - value
        if calc_result >= 0:
            water_count += calc_result

    return water_count


def trap_optimized(height: List[int]) -> int:
    if len(height) < 3:
        return 0

    water_count = 0
    height_len = len(height)
    left_pointer_index = 0
    right_pointer_index = height_len - 1
    max_left_pointer_value = 0
    max_right_pointer_value = 0

    while left_pointer_index < right_pointer_index:
        if height[left_pointer_index] <= height[right_pointer_index]:
            if height[left_pointer_index] > max_left_pointer_value:
                max_left_pointer_value = height[left_pointer_index]
            else:
                water_count += (
                    max_left_pointer_value - height[left_pointer_index]
                )
            left_pointer_index += 1
        else:
            if height[right_pointer_index] > max_right_pointer_value:
                max_right_pointer_value = height[right_pointer_index]
            else:
                water_count += (
                    max_right_pointer_value - height[right_pointer_index]
                )
            right_pointer_index -= 1

    return water_count


height_data = [4, 2, 0, 3, 2, 5]
trap_result = trap_optimized(height_data)

print(trap_result)
