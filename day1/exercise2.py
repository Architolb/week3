import re

my_emails = ["jordanw@codingtemple.orgcom", "pocohontas1776@gmail.com", "helloworld@aol..com", "yourfavoriteband@g6.org", "@codingtemple.com"]

pattern_email = re.compile('([a-z0-9]+)@([a-z0-9]+).(com|org)$')



for x in my_emails:
    
    if pattern_email.match(x):
        print(x)
    else:
        print(None)    



# found_emails = pattern_email.findall(my_emails[])
# print(found_emails)

