nums = []

for i in range(3):
    nums.append(int(input(f"Your {i+1} number: ")))

if nums[0] == nums[1] and nums[1] == nums[2]:
    print("All Same")
elif nums[0] != nums[1] and nums[1] != nums[2]:
    print("All different")
else:
    print("Neither")
