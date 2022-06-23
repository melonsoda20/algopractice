from typing import List, Tuple


def twoSum(numsInput: List[int], target: int) -> Tuple[List[int], None]:
    if len(numsInput) < 2:
        return None

    valMapTable = {}
    for index, value in enumerate(numsInput):
        desiredValue = target - value
        if desiredValue in valMapTable.keys():
            return [valMapTable[desiredValue], index]
        else:
            valMapTable[value] = index

    return None


nums = [3, 2, 4]
targetNum = 7

twoSumResults = twoSum(nums, targetNum)
print(twoSumResults)
