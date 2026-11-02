class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else :
                hash_map[char] = 0 
        
        for key, value in hash_map.items():
            if value == 0:
                index = s.find(key)
                return index
                break
        
        return -1

            