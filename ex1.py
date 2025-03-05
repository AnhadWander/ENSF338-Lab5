import sys

def evaluate_expression(exp):
    stack = []
    exp = exp.replace("(", " ( ")
    exp = exp.replace(")", " ) ")
    splitted = exp.split()


    for i in splitted:
        if i == ")":
            num2 = stack.pop()
            num1 = stack.pop()
            op = stack.pop()
            stack.pop() 

            if op == "+":
                stack.append(num1 + num2)
            elif op == "-":
                stack.append(num1 - num2)
            elif op == "*":
                stack.append(num1 * num2)
            elif op == "/":
                stack.append(int(num1 / num2))
        elif i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
            stack.append(int(i))
        else:
            stack.append(i)

    return stack.pop()



expression = sys.argv[1]
result = evaluate_expression(expression)
print(result)
