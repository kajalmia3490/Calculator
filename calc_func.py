def calc(values, operator):
    if operator == "+":
        sumation = 0
        for v in values:
            sumation = sumation + v
        return sumation
    elif operator == "-":
        return values[0] - values[1]
    elif operator == "*":
        multiplication = 1
        for v in values:
            multiplication = multiplication * v
        return multiplication
    elif operator == "/":
        for v in values:
            return values[0] / values[1]
    elif operator == "%":
        for v in values:
            return values[0] % values[1]
    else:
        return "Invalid Syntax!"