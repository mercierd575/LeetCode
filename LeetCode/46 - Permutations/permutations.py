from typing import List


# this recursive method will return all permutations of nums
def permute(nums: List[int]) -> List[List[int]]:
    answer: List[List[int]] = []
    if len(nums) <= 1:                              # base case
        return [nums[:]]
    for k in range(len(nums)):                      # for every possible starting num
        l: List[int] = [nums[k]]                    # l is a List[int] containing the starting num
        w: List[int] = nums[:k] + nums[k + 1:]      # w is a List[int] containing nums minus the starting num
        for p in permute(w):                        # every possible permutations after the first num
            answer.append(l + p)                    # are appended to answer List[List[int]]

    return answer
