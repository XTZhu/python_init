letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(letters[-5].title())

letters[0] = 'A'
print(letters)

letters.append('h')
print(letters)

letters.insert(0, '0')

print(letters)

del letters[0]
print(letters)

del_letter = letters.pop()
print(letters)
print(del_letter)

del_letter = letters.pop(0)
print(letters)
print(del_letter)

letters.remove('c')
print(letters)

letters.insert(2, 'z')
print(letters)

letters.sort()
print(letters)

# sort() function is  forever
letters.sort(reverse=True)
print(letters)

# sorted() function is temp
print(sorted(letters))
print(letters)

reversed_letters = letters.reverse()
print(reversed_letters)
print(letters)

print(len(letters))