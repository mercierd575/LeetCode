from typing import List


def constructTransformedArray(nums: List[int]):
    sol = nums[:]  # Copying the nums array into the result array
    for i in range(len(nums)):
        if nums[i] != 0:  # CASE 1 & 2: the value is not zero
            new_idx = (i + nums[i]) % len(nums)  # Translate the index using circular array logic
            sol[i] = nums[new_idx]  # Set the result value at i to the value of the nums array with the new index
        else:  # CASE 3: the value is zero
            sol[i] = nums[i]  # We simply set the result value to the corresponding value in the nums array
    return sol
