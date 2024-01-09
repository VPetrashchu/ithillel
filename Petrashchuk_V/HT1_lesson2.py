import math


#hometask_1
print('Hometask 1:')
student_firstname = 'Vasylyna'
student_lastname = 'Petrashchuk'
print('Student fullname: ' + student_firstname + ' ' + student_lastname)

student_fullname = student_firstname + ' ' + student_lastname
print(student_fullname.lower())
print(student_fullname.upper())
print(student_fullname.title())
student_fullname = '\t' + '     Real name:   '+ '\n' + student_firstname + '\n' + student_lastname
print(student_fullname)
print(student_fullname.strip())

#hometask_2
print('\n\nHometask 2:')
circle_radius = int(input('Enter digit of circle radius:'))
circle_area = str(round((math.pi * (circle_radius*circle_radius)), 0))
print(f' Area of a circle is ' + circle_area)


#hometask_3
print('\n\nHometask 3:')
current_usd = 38.45
convert_uah_to_usd = str(round((1000/current_usd), 2))
print('USD ' + convert_uah_to_usd + ' could buy for UAH 1000.')



