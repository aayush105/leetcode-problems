'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine 
if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''

def valid_parantheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return len(stack) == 0 

input = "()[]{}"
result = valid_parantheses(input)
print(result)
