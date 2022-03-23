class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        windowStart = 0
        max_avg = 0
        avg = 0
        c=0
        result = []
        windowSum = 0
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]
            if((windowEnd)>=k-1):
                avg = windowSum//k
                result.append(avg)
                windowSum -= arr[windowStart]
                windowStart += 1
        for i in range(len(result)):
            if(result[i]>=threshold):
                c=c+1
        return c