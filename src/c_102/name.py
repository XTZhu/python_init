name = 'ada_lovelace'

print(name.title())
print(name.upper())
print(name.lower())

first_name = 'sun'
last_name = 'wukong'

full_name = first_name.title() + '\n' + last_name;
print(full_name)

fool_input = 'python   '
# for end space
# meaning right strip
smart_input = fool_input.rstrip();
print(smart_input)

# lstrip() for left space
# strip() for both

age = 23

# wrong way
# can only concatenate str (not "int") to str
# message = "Happy " + age + "rd Birthday!"

# right way
message = "Happy " + str(age) + "rd Birthday!"

print(message)