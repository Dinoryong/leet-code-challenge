class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if haystack == "" and needle == "":
			return 0
		else:
			if needle in haystack:
				return(haystack.index(needle))
			else:
				return -1