def how_many_are_smaller(arr):
    count = 0
    result = []
    nums_in_arr = [i for i in arr]
    for i in range(len(arr)):
        for y in arr[i:]:
           if arr[i] > y:
               count += 1
        result.append(count)
        count = 0
    return result  

print(how_many_are_smaller([15, 1, 2, 0, 5, -1]))         

