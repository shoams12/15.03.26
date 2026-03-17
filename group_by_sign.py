#Write a function that groups numbers based on their sign
numbers = [4, -2, 0, 7, -5, 3]


def group_numbers(nums: list) -> dict:
    signs = {"positive": [], "negative": [], "zero": []}
    for num in nums:
        if num > 0:
            signs["positive"].append(num)
        elif num < 0:
            signs["negative"].append(num)
        else:
            signs["zero"].append(num)

    return signs


print(group_numbers(numbers))
