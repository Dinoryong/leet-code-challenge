class Solution:
      def isPowerOfThree(self, n):
        # brute force: make a power list with a for loop (max size is 20 so ~O(1) space)
        powers = [3**i for i in range(20)] # pow(3, i)
        return n in powers