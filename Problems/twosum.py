"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""
nums = [3,2,4,3]
target = 6
temp = []
def twosum(nums,target,temp):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                temp.append(i) 
                temp.append(j)
    return(temp)

print(twosum(nums,target,temp))