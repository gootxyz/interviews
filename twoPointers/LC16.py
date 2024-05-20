# 3 Sum Closest
def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float("inf")

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                return total

            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total

            if total < target:
                left += 1
            else:
                right -= 1

    return closest_sum


print(threeSumClosest(nums=[-1, 2, 1, -4], target=1))
