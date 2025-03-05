import sys

def eva_exp(exp):
    stack = []
    exp = exp.replace("(", " ( ")
    exp = exp.replace(")", " ) ")
    splitted = exp.split()


    for i in splitted:
        if i == ")":
            num2 = stack.pop()
            num1 = stack.pop()
            opr = stack.pop()
            stack.pop() 

            if opr == "+":
                stack.append(num1 + num2)
            elif opr == "-":
                stack.append(num1 - num2)
            elif opr == "*":
                stack.append(num1 * num2)
            elif opr == "/":
                stack.append(int(num1 / num2))
        elif i.isdigit() or (i[0] == "-" and i[1:].isdigit()):
            stack.append(int(i))
        else:
            stack.append(i)

    return stack.pop()



exp = sys.argv[1]
ans = eval_exp(exp)
print(ans)
