# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter the month as three characters (ie 'Jan', 'Feb'): ")
day = int(input("Enter the day of the month: "))

winter = ("Dec", "Jan", "Feb", "Mar") 
spring = ("Mar", "Apr", "May", "Jun") 
summer = ("Jun", "Jul", "Aug", "Sep") 
fall = ("Sep", "Oct", "Nov", "Dec") 

if month in winter:
    if(month == 'Dec' and day >=21) or (month == 'Mar' and day <= 19):
        print(f'{month} {day} is in the winter')
    elif(month == "Jan") or (month == "Feb"):
        print(f'{month} {day} is in the winter')
if month in spring:
    if(month == 'Mar' and day >=20) or (month == 'Jun' and day <= 20):
        print(f'{month} {day} is in the spring')
    elif(month == "Apr") or (month == "May"):
        print(f'{month} {day} is in the spring')
if month in summer:
    if(month == 'Jun' and day >=21) or (month == 'Sep' and day <= 21):
        print(f'{month} {day} is in the summer')
    elif(month == "Jun") or (month == "Jul"):
        print(f'{month} {day} is in the summer')
if month in fall:
    if(month == 'Sep' and day >=22) or (month == 'Dec' and day <= 20):
        print(f'{month} {day} is in the fall')
    elif(month == "Oct") or (month == "Nov"):
        print(f'{month} {day} is in the fall')

# if (month and day in winter):
#     print(f'{month} {day} is in the {season}')


