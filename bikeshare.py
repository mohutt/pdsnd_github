import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:\\Users\\Huetten\\udacity-git-course\\udacity-project\\chicago.csv',
              'new york city': 'C:\\Users\\Huetten\\udacity-git-course\\udacity-project\\new_york_city.csv',
              'washington': 'C:\\Users\\Huetten\\udacity-git-course\\udacity-project\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        if city not in ['chicago', 'new york', 'washington']:
            print('Please enter a valid city.\n')
        if city == 'new york':
            city = 'new york city'
            print('You have picked New York.\n')
            break
        else:
            print('You have picked {0}'.format(city.capitalize()), '\n')
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to see data for January, February, March, April, May, June or all? ').lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('Please enter a valid month or select all.')
        else:
            if month == 'all':
                print('You have picked all.\n')
            else:
                print('You have picked {0}'.format(month.capitalize()), '\n')
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to see data for a specific day of the week or all? ').lower()
        if day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            print('Please enter a valid day or select all.\n')
        else:
            if day == 'all':
                print('You have picked all.\n')
            else:
                print('You have picked {0}'.format(day.capitalize()), '\n')
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].value_counts().idxmax()
    popular_month = ['January', 'February', 'March', 'April', 'May', 'June'][month - 1]

    print('Most common month: ', popular_month)

    # display the most common day of week
    day = df['day_of_week'].value_counts().idxmax()

    print('Most common day of the week: ', day)


    # display the most common start hour
    df['Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    popular_hour = df['Hour'].value_counts().idxmax()

    print('Most common start hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].value_counts().idxmax()
    print('Most common start station: ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].value_counts().idxmax()
    print('Most common end station: ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start station and end station: ', popular_combo[0], ' and ', popular_combo[1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time:  ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n',
          'Subscriber: ',df['User Type'].value_counts()[0], '\n',
          'Customer:   ', df['User Type'].value_counts()[1], '\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of genders: \n',
              'Male:   ', df['Gender'].value_counts()[0], '\n',
              'Female: ', df['Gender'].value_counts()[1], '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(' The earliest year of birth is:    ', df['Birth Year'].min().astype(int), '\n',
              'The most recent year of birth is: ', df['Birth Year'].max().astype(int), '\n',
              'The most common year of birth is: ', df['Birth Year'].mode().astype(int)[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """displays raw data upon request"""
    response = input('Would you like to examine the raw data? If so, type yes: ')
    if response.lower() == 'yes':
        #set max_columns to display all columns to user
        pd.set_option('display.max_columns', 500)
        #set counter to iterate through lines of raw data
        n = 0
        while True:
            print(df[n: n + 5])
            n_response = input('Press Enter to continue viewing raw data. Type no to stop viewing raw data: ')
            n += 5
            #loop continues till user specifically states no
            if n_response == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
