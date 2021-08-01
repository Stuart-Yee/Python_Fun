x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

"""Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30"""

x[1][0] = 15
print(x)

print(sports_directory)

sports_directory["basketball"][1] = "Bryant"
print(sports_directory)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

print(z)
z[0]["y"] = 30
print(z)

##################################################

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dictList):
    for thisDictionary in dictList:
        element = 0
        line = ["",""]
        for key in thisDictionary.keys():
            line[element] = key + " - " + thisDictionary[key]
            element += 1
        print(line[0] + ", " + line[1])


iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for d in some_list:
        print(d[key_name])

iterateDictionary2("first_name", students)

iterateDictionary2('last_name', students)

def printInfo(listDictionary):
    keys = listDictionary.keys()
    for L in keys:
        print(len(listDictionary[L]), L.upper())
        for val in listDictionary[L]:
            print(val)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
"""
7
LOCATIONS
San
Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank

8
INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

