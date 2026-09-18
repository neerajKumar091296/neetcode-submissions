class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hash_map = {}

        for index in range(len(nums)):
            if nums[index] in hash_map and index - hash_map[nums[index]] <= k:
                return True
            hash_map[nums[index]] = index
        
        return False
