class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [] 
        curr_num = 0
        curr_string = ''
        
        for char in s:
            if char == '[':
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ''
                curr_num = 0
            elif char == ']':
                prev_num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + prev_num * curr_string
            elif char.isdigit():
                curr_num = curr_num * 10 + int(char)
            else:
                curr_string += char
        
        return curr_string