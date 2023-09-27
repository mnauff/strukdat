import math

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)

def precedence(operator):
    if operator in "^!":
        return 3
    elif operator in "*/":
        return 2
    elif operator in "+-":
        return 1
    else:
        return 0

def infix_to_postfix(expression):
    output = []
    operator_stack = Stack()
    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == "!":  # Factorial operator
            output.append(token)
        elif token in "+-*/^":  # Other operators
            while (
                not operator_stack.is_empty()
                and precedence(token) <= precedence(operator_stack.peek())
                and operator_stack.peek() != "("
            ):
                output.append(operator_stack.pop())
            operator_stack.push(token)
        elif token == "(":  # Left parenthesis
            operator_stack.push(token)
        elif token == ")":  # Right parenthesis
            while not operator_stack.is_empty() and operator_stack.peek() != "(":
                output.append(operator_stack.pop())
            operator_stack.pop()  # Remove the left parenthesis

    while not operator_stack.is_empty():
        output.append(operator_stack.pop())

    return "".join(output)

def evaluate_postfix(expression):
    operand_stack = Stack()
    for token in expression:
        if token.isalnum():  # Operand
            operand_stack.push(token)
        elif token in "+-*/^":  # Operator
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = calculate(operand1, operand2, token)
            operand_stack.push(result)
        elif token == "!":  # Factorial operator
            operand1 = operand_stack.pop()
            result = calculate(operand1, None, token)  # Pass None as operand2 for factorial
            operand_stack.push(result)
    return operand_stack.pop()

def calculate(operand1, operand2, operator):
    if operator == "+":
        return str(float(operand1) + float(operand2))
    elif operator == "-":
        return str(float(operand1) - float(operand2))
    elif operator == "*":
        return str(float(operand1) * float(operand2))
    elif operator == "/":
        if operand2 == 0:
            raise ValueError("Division by zero")
        else:
            return str(float(operand1) / float(operand2))
    elif operator == "^":
        return str(float(operand1) ** float(operand2))
    elif operator == "!":
        if operand1 is not None:
            return str(math.factorial(int(operand1)))
        else:
            return "Error: Factorial operand missing"



if __name__ == "__main__":
    while True:
        infix_expression = input("Enter an infix expression (or 'exit' to quit): ")
        
        if infix_expression.lower() == 'exit':
            break  # Exit the loop if the user enters 'exit'
        
        postfix_expression = infix_to_postfix(infix_expression)
        print("Postfix expression:", postfix_expression)

        result = evaluate_postfix(postfix_expression)
        print("Result:", result)