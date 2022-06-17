class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Consider each character in s as the centre of a palindrome.
        Check for the longest possible odd-length and even-length palindrome; store the longest palindrome
        """

        res, len_res, len_s = 0, 0, len(s)
        for i in range(len_s):
           
            odd, len_odd = i, 1
            for j in range(min(i, len_s-i-1)):   
                if s[i-j-1] != s[i+j+1]:        
                    break                        
                odd, len_odd = odd-1, len_odd+2  
            even, len_even = i, 0
            for j in range(min(i, len_s-i)):
                if s[i-j-1] != s[i+j]:
                    break
                even, len_even = even-1, len_even+2  
            len_res, res = max((len_res, res), (len_odd, odd), (len_even, even))
        return s[res:res+len_res]