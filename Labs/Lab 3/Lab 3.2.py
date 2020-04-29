month = input("Enter the month:")

if month in ('December', 'January', 'February'):
    season = 'winter'
    activity = 'snowboarding'
elif month in ('March', 'April', 'May'):
    season = 'spring'
    activity = 'hiking'
elif month in ('June', 'July', 'August'):
    season = 'summer'
    activity = 'swimming'
elif month in ('September', 'October', 'November'):
    season = 'autumn'
    activity = 'biking'
else:
    print("Please enter the correct season")

print("In",month,", it is", season, ", I suggest you go", activity)
