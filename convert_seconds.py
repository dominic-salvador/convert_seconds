import datetime

# Introduce user to the program and get user input
print('This program converts seconds to HH:MM:SS format.')
print('How many seconds do you want to convert?')
seconds_input = input('-> ')

# Process user input
seconds_input = int(seconds_input.strip())
converted_seconds = datetime.timedelta(seconds=seconds_input)
converted_seconds = str(converted_seconds)

# Print final result
print('\n%d seconds is equivalent to:' % seconds_input)
print(converted_seconds)
