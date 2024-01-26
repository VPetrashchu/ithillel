#Hometask#1
print('Hometask#1')

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

intersection = list(filter(lambda x: x in array1, array2))
print('Intersection of two arrays:', intersection)

#Hometask#2
print('Hometask#2')

is_number = lambda s: s.replace('.', '', 1).isdigit()

string1 = "123"
string2 = "12.34"
string3 = "abc"

print('Is the string a number?', is_number(string1))
print('Is the string a number?', is_number(string2))
print('Is the string a number?', is_number(string3))


#Hometask#3
print('Hometask#3')
strings = ['apple', 'banana', 'kiwi', 'orange']

max_min_length = lambda strings: [max(strings, key=len), min(strings, key=len)]

max_str, min_str = max_min_length(strings)
print('List with maximum and minimum length:', [min_str, max_str])



