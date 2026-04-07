class Solution:
    def isValid(self, s: str) -> bool:
        # given a string w/ brackets, goal we just need to check if they're all properly opened and closed in the right order
        # edge cases:
        # empty string -> return true 
        # single bracket -> return false
        # odd string lenght -> return false 
        
        # approahc: 
        # if empty, return true
        if not s:
            return True

        # if odd lenght, return false
        if len(s) % 2 != 0:
            return False

        # stack: to track opening brakcets - > use map
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        # loop thorugh each char (bracket)
        for char in s:

            # if its opening bracket, push onto stack
            if char in '([{':
                stack.append(char)

            # if closing bracket, check if stack is emtpy or the top of stack deons't match, return false
            else:
                if not stack or \
                    stack[-1] != matches[char]: 
                    return False 
                # otherwise pop the top -> found a valid pair
                stack.pop()

        # after loop, return true only if stack is empty -. everything matched
        return len(stack) == 0

        


