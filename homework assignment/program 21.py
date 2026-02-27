class Solution:
    def threeWayPartition(self, arr, a, b):
        n = len(arr)
        low = 0
        high = n - 1
        i = 0
        
        while i <= high:
            if arr[i] < a:
                arr[i], arr[low] = arr[low], arr[i]
                i += 1
                low += 1
            elif arr[i] > b:
                arr[i], arr[high] = arr[high], arr[i]
                high -= 1
            else:
                i += 1
        
        return arr
