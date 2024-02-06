number_list = list(map(int, input().split(", ")))

found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))

even_indicces = list(filter(lambda a: a != 'no', found_indices_or_no))
print(even_indicces)
