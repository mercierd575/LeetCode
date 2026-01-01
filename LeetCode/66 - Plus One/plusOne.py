def plusOne(digits):
    # CASE A: Last digit is less than nine.
    # In that case, we just need to increment that digit.
    if digits[len(digits) - 1] < 9:
        digits[len(digits) - 1] += 1
        return digits
    # CASE B: last digit is nine.
    # In that case, we need to figure out what the other digits
    # before that look like.
    else:
        i = len(digits) - 1
        # Going through the digits until we find one that isn't 9
        # or until we reach the start of the list.
        while i > 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1
        # We check if the last digit checked is the start of the list
        # and is equal to 9. In that case, we need to add a new digit
        # at the start of the list.
        if i == 0 and digits[i] == 9:
            digits[i] = 0
            return [1] + digits
        # Otherwise, we increment the last digit we looked at.
        else:
            digits[i] += 1
            return digits

print(plusOne([1, 2, 3]) == [1, 2, 4])
print(plusOne([9, 9]) == [1, 0, 0])
print(plusOne([8, 9, 9]) == [9, 0, 0])
