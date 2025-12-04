def sortArray(nums):
        swapped = False
        for i in range(len(nums)-1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums


nums = [17,23,89,68,2,4,12,67,85]

print(sortArray(nums=nums))