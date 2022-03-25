class Solution:
    def longestPalindrome(self, s: str) -> str:
        for win_size in range(len(s), 0, -1):
            start=0
            end=win_size
            while(start+win_size<=len(s)):
                word=s[start:end]
                if word==word[::-1]:
                    return word
                start=start+1
                end=end+1
        return largest_pdrome
        