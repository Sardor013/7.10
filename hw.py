#11
'''def reverse_middle(lst):
    if len(lst) < 4:
        raise ValueError("The list must contain at least four elements.")

    mid_index = len(lst) // 2

    if len(lst) % 2 == 0:
        middle_elements = lst[mid_index-1:mid_index+1]
    else:
        middle_elements = lst[mid_index-1:mid_index+2]

    return middle_elements[::-1]

lst = [1, 2, 3, 4, 5, 6, 7]
print(reverse_middle(lst)) '''



#12
'''def partlist(arr):
    if len(arr) < 2:
        raise ValueError("The list must contain at least two elements.")

    result = []
    for i in range(1, len(arr)):
        part1 = ' '.join(arr[:i])
        part2 = ' '.join(arr[i:])
        result.append((part1, part2))

    return result

a = ["az", "toto", "picaro", "zone", "kiwi"]
print(partlist(a))
'''


#13
'''def or_arrays(arr1, arr2, default=0):
    max_len = max(len(arr1), len(arr2))

    extended_arr1 = arr1 + [default] * (max_len - len(arr1))
    extended_arr2 = arr2 + [default] * (max_len - len(arr2))

    result = [a | b for a, b in zip(extended_arr1, extended_arr2)]

    return result'''



#14
'''def remove_smallest(arr):
    if not arr:
        return []

    min_value = min(arr)
    min_index = arr.index(min_value)

    return arr[:min_index] + arr[min_index + 1:]'''


#15
'''def bear_fur(parents):
    offspring_colors = {
        ('black', 'black'): 'black',
        ('brown', 'brown'): 'brown',
        ('white', 'white'): 'white',
        ('black', 'brown'): 'dark brown',
        ('brown', 'black'): 'dark brown',
        ('black', 'white'): 'grey',
        ('white', 'black'): 'grey',
        ('brown', 'white'): 'light brown',
        ('white', 'brown'): 'light brown'
    }

    parent1, parent2 = parents

    return offspring_colors.get((parent1, parent2), 'unknown')'''

