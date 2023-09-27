import math

def infix_to_postfix(expression):
    def precedence(operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/', '%'):
            return 2
        elif operator == '^':
            return 3
        elif operator == '!':
            return 4
        return 0

    def is_operator(token):
        return token in "+-*/%^!"

    def infix_to_postfix_internal(expression):
        stack = []
        postfix = []
        tokens = expression.split()

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack:
                    raise ValueError("Mismatched parentheses")
                stack.pop()  # Pop the '('
            elif is_operator(token):
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                    postfix.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            postfix.append(stack.pop())

        return ' '.join(postfix)

    postfix_expression = infix_to_postfix_internal(expression)
    return postfix_expression

def postfix_calculator(expression):
    def is_operator(token):
        return token in "+-*/%^!"
    def apply_operator(operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("Division by zero")
            return operand1 / operand2
        elif operator == '^':
            return operand1 ** operand2
        elif operator == "!":
            if operand1 is not None:
                return str(math.factorial(int(operand1)))
            else:
                return "Error: Factorial operand missing"

    stack = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token == '!':
            if len(stack) < 1:
                raise ValueError("Insufficient operands for operator !")
            operand = stack.pop()
            result = apply_operator(token, operand, 0)
            stack.append(result)
        elif is_operator(token):
            if len(stack) < 2:
                raise ValueError("Insufficient operands for operator {}".format(token))
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(token, operand1, operand2)
            stack.append(result)
        else:
            raise ValueError("Invalid token: {}".format(token))

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]

while True:
    user_expression = input("Masukkan operasi: ")
    
    if user_expression.lower() == 'exit':
        break

    try:
        postfix_expression = infix_to_postfix(user_expression)
        print("Postfix expression:", postfix_expression)
        result = postfix_calculator(postfix_expression)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
