nums = [1,2,3]
print(type(nums))

nums.append(7)
nums.append(9)
nums.append(300)
print(len(nums))

nums[3] = 200 
nums.insert(0,-200)
print(nums[6])
print(nums[-1])
print(nums[-2])
print(2 in nums)
print(nums)