class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_total = nums[0]

        for i in nums[1:]:
            if current_sum < 0:
                current_sum = i
            else:
                current_sum += i
            
            if current_sum > max_total:
                max_total = current_sum
        
        return max_total
        
        