def unique_in_order(element):
    element_listed = [i for i in element]
    for i in range(1,len(element_listed)):
        if i < len(element_listed):
            while i != len(element_listed) and element_listed[i-1] == element_listed[i]:
                element_listed.pop(i)
    return element_listed

print(unique_in_order('AAAABBBCCDAABBB'))            