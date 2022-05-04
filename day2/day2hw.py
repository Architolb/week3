

# Exercise#1 Filter out all of the empty strings from the list below
from re import X


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
x = []
for i in places:
    if i.strip() != '':
        x.append(i)
print(x)

# exercise#2 Write an anonymous function that sorts this list by the last name... 
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
x = sorted(author, key=lambda name: name.split(" ")[-1].lower())
print(x)

# exercise#3 Convert the list below from Celsius to Farhenheit, using the map function with a lambda.
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
Fahrenheit = map(lambda y: (float(9)/5)*y + 32, places)
print(Fahrenheit)

# Can't figure out how to add in the locations

# exercise4 Write a recursion function to perform the fibonacci sequence up to the number passed in.
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

nterms = 21
for i in range(nterms):
       print(fibonacci(i))