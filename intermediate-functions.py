# 1 Update Values in Dictionaries and Lists

from typing import ValuesView

"""1"""

x = [[5, 2, 3], [10, 8, 9]]
student = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# ---1
for i in x:
    if i[0] == 10:
        i[0] = 15
print(x)

# -----2
student = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}]
print(student)
# for l in students:
#     if l['lastname'] == ['Jordan']:
#         l['last_name'] = ['Bryant']
# print(students)

# ----3
sports_directory['soccer'] = {'Andres', 'Ronaldo', 'Rooney'}
print(sports_directory)
# 4
z = [{'x': 10, 'y': 30}]
print(z)

"""2"""
students = [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]

def interateDictionary(some_list):
    for i in some_list:
        if i:
            sorted_keys = sorted(list(i.keys()))
            pairs = [f"{k} - {i[k]}" for k in sorted_keys]
            s = ", ".join(pairs)
            return s
print(interateDictionary(students))



def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

"""3"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']), "locations")
    for location in some_dict['locations']:
        print(location)
    print(len(some_dict['instructors']), "instructors")
    for location in some_dict['instructors']:
        print(location)
print(printInfo(dojo))







