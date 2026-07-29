from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    answer: List[List[int]] = []
    if len(nums) <= 1:
        return [nums[:]]
    for k in range(len(nums)):
        l: List[int] = [nums[k]]
        w: List[int] = nums[:k] + nums[k + 1:]
        for p in permute(w):
            answer.append(l + p)

    return answer