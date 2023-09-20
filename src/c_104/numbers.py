numbers = range(1, 4)
print(numbers)

numbers_list = list(numbers)

print(numbers_list)

print(numbers_list[0:3])

even_numbers = list(range(2, 11, 2))
print(even_numbers)


print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))

# short way

odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)
