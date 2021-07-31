num1 = 42 #variable declaration
num2 = 2.3 #varaiable declaration
boolean = True #variable declaration
string = 'Hello World' #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration - list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration - dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration - tuple
print(type(fruit)) #log (printing) the type check of a variable
print(pizza_toppings[1]) #log statement of the second element of a list
pizza_toppings.append('Mushrooms') #method to add a value to the end of a list
print(person['name']) #log statement from a dictionary
person['name'] = 'George' #assigning a new key/value pair to a dictionary
person['eye_color'] = 'blue' #asssigning a new key/value pair to a dictionary
print(fruit[2])

if num1 > 45: #conditional statement compararing a variable to a fixed value
    print("It's greater") #log statement
else: #conditional statement if above test not met
    print("It's lower") #log statement

if len(string) < 5: #conditional statement comparing the length of a string to a fixed value
    print("It's a short word!") #log statement
elif len(string) > 15: #else if conditional if above condition not met
    print("It's a long word!") #log statement
else: # conditional if above conditions not met
    print("Just right!")  #log statement

for x in range(5): #for loop - five tiems
    print(x) # log statement
for x in range(2,5): #for loop 2 to 5 (start and stop)
    print(x) # log statement
for x in range(2,10,3): #for lopp with a start, stop and increment
    print(x) #log statement
x = 0 #variable reassignment
while(x < 5): #while loop
    print(x) #log statement
    x += 1 #increment

pizza_toppings.pop() #remove item from end of a list
pizza_toppings.pop(1) #remeove second element from a list

print(person) #log statement
person.pop('eye_color') #remove element from dictionary
print(person) #log statement

for topping in pizza_toppings: #for loop through list
    if topping == 'Pepperoni': #conditional comparator
        continue #continue statement (starts next loop)
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional comparator
        break #break - terminates loop

def print_hello_ten_times(): #function declaration
    for num in range(10): #function statements - for loop 10 times
        print('Hello') #log statement

print_hello_ten_times()  #functiona call

def print_hello_x_times(x): #function declaration with argument
    for num in range(x): #function statement (for loop)
        print('Hello') #log statement

print_hello_x_times(4) #function call with argument

def print_hello_x_or_ten_times(x = 10): #function declaraiton with argument with assigned value
    for num in range(x): #for loop
        print('Hello')  #log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)