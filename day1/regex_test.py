import re
# import re
# import .txt file ofr exercise
# setup with open statement
# print title of list for clarity
# looking for the last name
# only print if name is capped correctly
# if not not configured correctly return 'NONE'
# separate solution into groups
# using match to find the correct setup for the last name
# 
with open('day1/regex.txt') as file:
    names = file.readlines()

print('==============\nLast Name\n==============')

for person in names:
    test = re.match(r'([\w\W])* ([A-Z][A-Za-z]+)$', person) 
    if test:
        print(f'{test.groups()[1]}\n')
    else:
        print('NONE')
    
