def simple_fun(formula):
    if 7 not in formula and 8 not in formula:
        return False
    elif 1 in formula and 2 in formula:
        return False
    elif 3 in formula and 4 in formula:
        return False
    elif 5 in formula and 6 not in formula:
        return False
    elif 6 in formula and 5 not in formula:
        return False
    return True

print(simple_fun([5,6,7]))