import time
import pandas as pd
import numpy as np

CITY_DATA = {
  'chicago': 'chicago.csv',
  'new york city': 'new_york_city.csv',
  'washington': 'washington.csv'
}

def get_filters():
  ""
"
Asks user to specify a city, month, and day to analyze.

Returns:
  (str) city - name of the city to analyze(str) month - name of the month to filter by, or "all"
to apply no month filter
  (str) day - name of the day of week to filter by, or "all"
to apply no day filter
  ""
"
print('Hello! Let\'s have some fun and explore some US bikeshare data!')# TO DO: get user input
for city(chicago, new york city, washington).HINT: Use a
while loop to handle invalid inputs
city = input('\nWould you like to analyize the data for Chicago, New York, Washington or All?\n').lower()

while (True):
  if (city == 'chicago'
    or city == 'new york'
    or city == 'washington'
    or city == 'all'):
    break
else :
  city = input('Please Enter Correct City: ').lower()

# TO DO: get user input
for month(all, january, february, ..., june)
month = input('\nWhich month would you like to analyize? Jan, Feb, Mar, Apr, May, Jun or All?\n').lower()
while (True):
  if (month == 'jan'
    or month == 'feb'
    or month == 'mar'
    or month == 'apr'
    or month == 'may'
    or month == 'jun'
    or month == 'all'):
    break
else :
  month = input('Please enter a valid month\n').lower()

# TO DO: get user input
for day of week(all, monday, tuesday, ...sunday)

day = input('\nWhich day would you like to analyize? Mon, Tue, Wedn, Thu, Fri, Sat, Sun or All?\n').lower()

while (True):
  if (day == 'mon'
    or day == 'tue'
    or day == 'wed'
    or day == 'thu'
    or day == 'fri'
    or day == 'sat'
    or day == 'sun'
    day == 'all'):
    break
else :
  month = input('Please enter a valid day\n').lower()

print('-' * 40)
return city, month, day

def load_data(city, month, day):
  ""
"
Loads data
for the specified city and filters by month and day
if applicable.

Args:
  (str) city - name of the city to analyze(str) month - name of the month to filter by, or "all"
to apply no month filter
  (str) day - name of the day of week to filter by, or "all"
to apply no day filter
Returns:
  df - Pandas DataFrame containing city data filtered by month and day ""
"

return df

def time_stats(df):
  ""
"Displays statistics on the most frequent times of travel."
""

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

# TO DO: display the most common month
if (month == 'all'):
  most_common_month = df['Start Time'].dt.month.value_counts().idxmax()
print('Most common month is ' + str(most_common_month))

# TO DO: display the most common day of week
if (day == 'all'):
  most_common_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
print('Most common day is ' + str(most_common_day))

# TO DO: display the most common start hour
most_common_hour = df['Start Time'].dt.hour.value_counts().idxmax()
print('Most popular hour is ' + str(most_common_hour))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)

def station_stats(df):
  ""
"Displays statistics on the most popular stations and trip."
""

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

# TO DO: display most commonly used start station
most_commonly_used_start_station = st.mode(df['Start Station'])
print('\nMost common start station is {}\n'.format(most_commonly_used_start_station))

# TO DO: display most commonly used end station
most_commonly_used_end_station = st.mode(df['End Station'])
print('\nMost common end station is {}\n'.format(most_commonly_used_end_station))

# TO DO: display most frequent combination of start station and end station trip
Most_frequent_combination_for_start_and_stop_stations = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
most_frequent_combination = Most_frequent_combination_for_start_and_stop_stations.value_counts().idxmax()
print('\nMost frequent combination for start and stop stations {}\n'.format(Most_frequent_combination_for_start_and_stop_stations))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)

def trip_duration_stats(df):
  ""
"Displays statistics on the total and average trip duration."
""

print('\nCalculating Trip Duration...\n')
start_time = time.time()

# TO DO: display total travel time
total_travel_time = df['Travel Duration'].sum()
time_total = total_travel_time
day = time_total // (24 * 3600)
time_total = time_total % (24 * 3600)
hour = time_total // (60 * 3600)
time_total %= 3600
minutes = time_total // 60
time_total %= 60
seconds = time_total
print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))

# TO DO: display mean travel time
total_travel_time = df['Travel Duration'].mean()
time_mean = total_travel_time
day = time_mean // (24 * 3600)
time_mean = time_mean % (24 * 3600)
hour = time_mean // (60 * 3600)
time_mean %= 3600
minutes = time_mean // 60
time_mean %= 60
seconds = time_mean
print('\nMean travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)

def user_stats(df):
  ""
"Displays statistics on bikeshare users."
""

print('\nCalculating User Stats...\n')
start_time = time.time()

# TO DO: Display counts of user types

no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
no_of_customers = df['User Type'].str.count('Customer').sum()
print('\nNumber of subscribers {}\n'.format(int(no_of_subscribers)))
print('\nNumber of customers {}\n'.format(int(no_of_customers)))

# TO DO: Display counts of gender

if ('Gender' in df):
  male_count = df['Gender'].str.count('Male').sum()
female_count = df['Gender'].str.count('Female').sum()
print('\nNumber of Male users {}\n'.format(int(male_count)))
print('\nNumber of Female users {}\n'.format(int(female_count)))

# TO DO: Display earliest, most recent, and most common year of birth
if ('Birth Year' in df):
  earliest_year = df['Birth Year'].min()
most_recent_year = df['Birth Year'].max()
most_common_year = st.mode(df['Birth Year'])
print('\nEarliest Birth Year is {}\nMost Recent Birth Year is {}\nMost Common Birth Year is {}\n'.format(int(earliest_year), int(most_recent_year).int(most_common_year)))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)

def main():
  while True:
  city, month, day = get_filters()
df = load_data(city, month, day)

time_stats(df)
station_stats(df)
trip_duration_stats(df)
user_stats(df)

restart = input('\nWould you like to restart? Enter yes or no.\n')
if restart.lower() != 'yes':
  break

if __name__ == "__main__":
  main()