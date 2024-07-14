def Age_Range_Compatibility(age):
    min = 0
    max = 0
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    elif age > 14:
        min = age // 2 + 7
        max = (age - 7) * 2
    return f'{int(min)}-{int(max)}'   

print(Age_Range_Compatibility(17))     

