list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

l_max = list_numbers[0]
max_i = 0
for i in range(19):
    if list_numbers[i] > l_max:
        l_max = list_numbers[i]
        max_i = i
list_numbers[max_i], list_numbers[19] = list_numbers[19], list_numbers[max_i]
print(list_numbers)