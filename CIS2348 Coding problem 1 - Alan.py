#Alan Escamilla 1167344#

print("Alan's Birthday Calculator")
print("To begin, please enter the current date")
print('Current Day')
current_month = int(input('Month:\n'))
current_day = int(input('Day:\n'))
current_year = int(input('Year:\n'))
print("Month:", current_month)
print("Day:", current_day)
print("Year:", current_year)
print("Today's date", current_month,'/', current_day,'/',current_year)

print('Now enter your birthdate:')
user_birthmonth = int(input('Month:\n'))
user_birthday = int(input('Day:\n'))
user_birthyear = int(input('Year:\n'))


print("Month:", user_birthmonth)
print("Day:", user_birthday)
print("Year:", user_birthyear)
print("Your birthdate", user_birthmonth,'/', user_birthday,'/',user_birthyear)



if current_day == user_birthday and current_month == user_birthmonth:
    print("Happy Birthday!!")

real_age = current_year - user_birthyear -((current_month, current_day) < (user_birthmonth, user_birthday))


print('You are ', real_age, 'years old.')