'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

'''

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in ['+', '-', '*', '/']:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            else:
                if operand1 * operand2 or operand1 % operand2 != 0:
                    result = operand1 // operand2 + 1
                else:
                    result = operand1 // operand2
            stack.append(result)
    return stack[-1]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output = eval_rpn(tokens)
print("Output: ", output)