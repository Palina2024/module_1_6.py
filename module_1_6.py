a = 'work this a dictionary'
print(a.upper())
my_dict = {'Palina': 1998, 'Irina': 2002,'Roman': 1988, 'Max':2000}
print('dict:', my_dict)
print("Max's year of birth:", my_dict['Max'])
my_dict['Dima'] = 1990
print(my_dict)
my_dict.update({'Sasha': 1995,
                'Masha': 1985})
print(my_dict.pop('Palina'))
print('modified dict', my_dict)
a= ' '
print(a)
a= 'work this a set'
print((a.upper()))
my_set = {'a', 'b', 'c', 1, 1, 5, 5, 'b'}
print('set:', my_set)
my_set.update({'f', 2})
my_set.remove('a')
print('modified set', my_set)
