class Solution:
    def kthMissing(self, arr, k):
        # Binary search se missing number find karenge
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            # arr[mid] tak kitne numbers missing hain?
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                # K aur missing ke beech abhi gap hai
                low = mid + 1
            else:
                # K missing number mid ke left side mein hoga
                high = mid - 1
        
        # Answer hamesha low + k hoga
        return low + k
