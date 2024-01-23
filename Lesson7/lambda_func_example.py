def func_name():
    pass

double = lambda x: x*2

print(double(2))
print(double(3))
print(double(4))

def func_double(x):
    return x*2

def to_cube(x):
    return x*x*x

lambda_to_cube = lambda x: x*x*x

print(to_cube(3))
print(lambda_to_cube(3))

lambda_multiple_tree = lambda a,b,c: a*b*c
print(lambda_multiple_tree(3,5,9))


import math
sqrt_x = lambda x: math.sqrt(x)
print(sqrt_x(9))

lambda_list = [
    lambda x: x*2,
    lambda x: x*3,
    lambda x: x*4,
]

print(lambda_list[0](2))
for el in lambda_list:
    print(el(6))

lambda_tuple = (
    lambda x: x*x,
    lambda x: x*x*x,
    lambda x: x*x*x*x,
)

for el in lambda_tuple:
    print(el(10))

areas_dic = {
    'circle' : lambda  r: math.pi*r*r,
    'rectangle' : lambda  a,b: a*b,
    'square' : lambda  a: a*a,
}

print(areas_dic['square'](4))
print(areas_dic['rectangle'](12, 15))
print(areas_dic['circle'](6))

list_a = [1,2,3,4,5,6,7,8,9,10,11]
filtered_list = list(filter(lambda x: x%2 ==0, list_a))
print(filtered_list)

filtered_odd_list = list(filter(lambda x: x%2==1, list_a))
print(filtered_odd_list)

double_list = list(map(lambda x: x*2, list_a))
print(double_list)
double_list_but_in_different_way = list(map(func_double, list_a))
print(double_list_but_in_different_way)

#triple_list = list(map(lambda a,b,c: a+b+c, list_a, list_a, list_a)) те саме, шо і 67 р
#print(triple_list)

print(func_double(2))
print(func_double)

from functools import reduce
sub_body = reduce(lambda x,y:x+y, list_a)
print(sub_body)


list_b = [90,50,50,60,45,75]
min_el= reduce(lambda a,b: a if(a<b) else b, list_b)

min_el_but= reduce(min, list_b)
print(min_el)
print(min_el_but)

list_c = [[15,9,45], [45,67,23], [87,3,9]]
sorted_list = lambda x: (sorted(el) for el in x)
print(list(sorted_list(list_c)))
# задача 1 - вивести всі елементі від найменшого до найбільшого в одному масиві; 2- сортувати ліст за сумами від найменшого до найбільшого