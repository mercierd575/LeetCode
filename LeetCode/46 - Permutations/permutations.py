from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = [[]]
    if len(nums) <= 2:
        return [nums[::-1]]
    for num in nums:
        result.append(nums[:num] + nums[num:])

    pos = 0

    for option in result:
        pos += 1
        posY = 0
        for answer in result:
            if option == answer and pos != posY:
                result = result[:posY] + result[posY:]
            posY += 1

    return result
