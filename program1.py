class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string
        for char in s:
            # If it's an opening bracket, push it to the stack
            if char in matching_bracket.values():
                stack.append(char)
            # If it's a closing bracket
            elif char in matching_bracket:
                # Check if the stack is not empty and the top matches the corresponding opening bracket
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()  # Pop the matched opening bracket
                else:
                    return False  # Invalid bracket sequence
            else:
                return False  # Invalid character (if any other than the allowed ones)
        
        # If the stack is empty, all brackets were matched; otherwise, it's invalid
        return len(stack) == 0


sol = Solution()
