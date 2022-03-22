class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        threshold = threshold * k
        ans = 0
        k_sum = sum(arr[:k])
        if k_sum >= threshold:
            ans += 1
        for i in range(k, len(arr)):
            k_sum -= arr[i-k]
            k_sum += arr[i]
            if k_sum >= threshold:
                ans += 1
        return ans