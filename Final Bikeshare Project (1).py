#!/usr/bin/env python
# coding: utf-8

# In[63]:


import time
import pandas as pd
import numpy as np


# In[64]:


import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'}

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    city = ""
    month = ""
    day = ""

    print('Hello! Let\'s explore some US bikeshare data.')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new York City', 'washington']
    while True:
        city = input("Please enter a city (all, Chicago, New York City, Washington): ").strip().lower()

        if city in cities:
            break
        else:
            print("Invalid input. Please enter one of the provided city names.")

    print(f'You selected {city} as your city.')

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july']
    while True:
        month = input("Please enter a month (all, January, February, March, April, May, June, July): ").strip().lower()

        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or 'All'.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while True:
        day = input("Please enter a day of the week (all, Monday, Tuesday, ..., Sunday): ").strip().lower()

        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day of the week or 'All'.")

    print('-'*40)

    return city, month, day


# In[65]:


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
    
    data_file = CITY_DATA[city.lower()]  # Get the corresponding data file
    df = pd.read_csv(data_file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    return df


# In[66]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    time_stats_result = {}

    # display the most common month
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    time_stats_result['most_popular_hour'] = popular_hour
    print("Most common hour: {}". format(popular_hour))

    # display the most common day of week
    df['week'] = df['Start Time'].dt.isocalendar().week
    popular_week = df['week'].mode()[0]
    time_stats_result['most_popular_week'] = popular_week
    print("Most common week: {}". format(popular_week))

    # display the most common start hour
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    time_stats_result['most_popular_month'] = popular_month
    print("Most common month: {}". format(popular_month))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[67]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_starttime = df['Start Station'].mode()[0]
    print("The most common start time of travel is: {}".format(common_starttime))

    # display most commonly used end station
    common_endtime = df['Start Station'].mode()[0]
    print("The most common end time of travel is: {}".format(common_endtime))

    # display most frequent combination of start station and end station trip
    combination = df['Start Station'].mode()[0] + " TO " + df['End Station'].mode()[0]
    print("The most frequent combination of start station and end station trip is: {}".format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[68]:


def trip_duration_stats(df):
    """Calculates statistics on the total and average trip duration."""
    
    # Initialize the dictionary to store the statistics
    trip_duration_stats_result = {}

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time
    total_travel_time = df['Trip Duration'].sum()
    trip_duration_stats_result['total_travel_time'] = total_travel_time
    print("Total travel time: {} seconds".format(total_travel_time))

    # Calculate mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    trip_duration_stats_result['mean_travel_time'] = mean_travel_time
    print("Total travel time: {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[69]:


def user_stats(df):
    
    user_stats_result = {}

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate counts of user types
    user_types = df['User Type'].value_counts()
    user_stats_result['user_type_counts'] = user_types.to_dict()

    # Calculate counts of gender
    gender = df['Gender'].value_counts()
    user_stats_result['gender_counts'] = gender.to_dict()

    # Calculate earliest, most recent, and most common year of birth
    earliest_yob = int(df['Birth Year'].min())
    most_recent_yob = int(df['Birth Year'].max())
    common_yob = int(df['Birth Year'].mode()[0])
    user_stats_result['earliest_year_of_birth'] = earliest_yob
    user_stats_result['most_recent_year_of_birth'] = most_recent_yob
    user_stats_result['most_common_year_of_birth'] = common_yob
    
    print(user_stats_result)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[70]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            start_index = 0
            while start_index < len(df):
                end_index = start_index + 5
                print(df.iloc[start_index:end_index])
                more_raw_data = input('\nWould you like to see more raw data? Enter yes or no.\n')
                if more_raw_data != 'yes':
                    break
                start_index = end_index

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:




