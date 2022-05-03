Hawkins, Derek	derek@codingtemple.com	(555) 555-5555	Teacher, Coding Temple	@derekhawkins
Zhai, Mo	mozhai@codingtemple.com	(555) 555-5554	Teacher, Coding Temple
Johnson, Joe	joejohnson@codingtemple.com		Johson, Joe
Osterberg, Sven-Erik	governor@norrbotten.co.se		Governor, Norrbotten	@sverik
, Tim	tim@killerrabbit.com		Enchanter, Killer Rabbit Cave
Butz, Ryan	ryanb@codingtemple.com	(555) 555-5543	CEO, Coding Temple	@ryanbutz
Doctor, The	doctor+companion@tardis.co.uk		Time Lord, Gallifrey
Exampleson, Example	me@example.com	555-555-5552	Example, Example Co.	@example
Pael, Ripal	ripalp@codingtemple.com	(555) 555-5553	Teacher, Coding Temple	@ripalp
Vader, Darth	darth-vader@empire.gov	(555) 555-4444	Sith Lord, Galactic Empire	@darthvader
Fernandez de la Vega Sanz, Maria Teresa	mtfvs@spain.gov		First Deputy Prime Minister, Spanish Gov

import re




with open('names.txt') as file:
    data = file.readlines()

print('==============\nFull Name / Twitter\n==============')
# goal is just to capture the last name, first name, and twitter handle as separate capture groups
for person in data:
    test = re.match(r'([\w]+), ([\w-]+)[\w\W]*\s(@[A-Za-z0-9]+)$', person) 
    if test:
        print(f'{test.groups()[1]} {test.groups()[0]} / {test.groups()[2]}', end='\n\n')


           