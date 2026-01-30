def remove_duplicates(nums):
    if not nums:
        return 0

    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    return index

arr = [1, 1, 2, 2, 3]
print("Unique count:", remove_duplicates(arr))
