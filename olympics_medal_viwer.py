"""
Program: Olympics 2024 Medals Viewer

Description:
This Python program allows users to explore Olympic medal data from the 2024 games,
using a CSV file as input. The program provides the following functionalities:
1. Display a country ranking based on total medals.
2. Show the medals won by athletes from a specific country in various sports.
3. List all athletes who won medals in a chosen sport, either globally or for a specific country.
4. Save the filtered data as a CSV file for future analysis.

The data is sourced from https://olympics.com/en/paris-2024/medals and stored in an input CSV file (olympics2024.csv).

Author: [Marcelo Carteri de Assumpção]
"""

import pandas as pd

# Function to display the ranking of countries based on the number of medals,
# prioritizing gold medals, followed by silver, and then bronze in case of ties.
def country_rank():
    rank_df = df.groupby('Country')[['Gold', 'Silver', 'Bronze']].sum()  # Summing medals by country
    rank_df['Total'] = rank_df['Gold'] + rank_df['Silver'] + rank_df['Bronze']  # Adding a total medals column
    rank_df = rank_df.sort_values(['Gold', 'Silver', 'Bronze'], ascending=False)  # Sorting by medal count

    rank_df = rank_df.reset_index()  # Resetting index
    rank_df.index = rank_df.index + 1  # Setting index to start from 1 instead of 0

    print(rank_df)  # Displaying the ranking of countries
    save_csv(rank_df)  # Option to save the filtered data

# Function to display all sports where a country won medals
def sports_country():
    while True:
        print('Please enter the name of a country to see all sports with medalists:')
        print(df['Country'].unique())  # Listing all available countries
        country = input()
        if country in df['Country'].values:
            # Grouping the data by sport for the selected country
            rank_df = df[df['Country'] == country]
            rank_df = rank_df.groupby('Sport')[['Gold', 'Silver', 'Bronze']].sum()
            rank_df['Total'] = rank_df['Gold'] + rank_df['Silver'] + rank_df['Bronze']  # Calculating total medals
            print(rank_df)  # Displaying the results

            save_csv(rank_df)  # Option to save the filtered data
            break
        else:
            print('Invalid country. Please enter the name as it appears in the list.')


# Function to display medalist athletes for a selected sport, either globally or for a specific country
def athletes_sport():
    specific = None
    while True:
        print('Do you want to see all medalists of a sport or just from a specific country?')
        print('1- All')
        print('2- Specific')
        answer = input()

        if answer == '1':
            specific = False  # User chooses to see athletes from all countries
            break
        elif answer == '2':
            specific = True  # User chooses to see athletes from a specific country
            break
        else:
            print('Invalid option, please choose 1 or 2.')  # Prompting user to choose a valid option

    if specific:
        # Asking for the name of a specific country
        while True:
            print('Please enter the name of a country to see the medalists from that country:')
            print(df['Country'].unique())  # Listing all available countries
            country = input()
            if country in df['Country'].values:
                break
            else:
                print('Invalid country. Please enter the name as it appears in the list.')

    # Asking for the name of the sport
    while True:
        print('Please enter the name of a sport to see all medalists athletes:')
        print(df['Sport'].unique())  # Listing all available sports
        sport = input()
        if sport in df['Sport'].values:
            # Filtering the data for the selected sport
            rank_df = df[df['Sport'] == sport]
            if specific:
                # Filtering further if the user chose a specific country
                rank_df = df[(df['Sport'] == sport) & (df['Country'] == country)]
                if rank_df.empty:
                    print(f'No medalists found from {country} in {sport}')  # Message if no athletes found
                else:
                    print(rank_df[['Sport', 'Modality - Athlete', 'Country', 'Gold', 'Silver',
                                   'Bronze']].to_string(index=False))  # Display results
                    save_csv(rank_df)  # Option to save the filtered data
            else:
                print(rank_df[['Sport', 'Modality - Athlete', 'Country', 'Gold', 'Silver',
                               'Bronze']].to_string(index=False))  # Display results for all countries
                save_csv(rank_df)  # Option to save the filtered data
            break
        else:
            print('Invalid sport. Please enter the name as it appears in the list.')


# Function to save the DataFrame to a CSV file with user-defined name
def save_csv(data):
    while True:
        print("Would you like to save this data to a CSV file? (yes/no)")
        answer = input().lower()

        if answer == 'yes':
            print("Enter the desired file name (without extension):")
            filename = input()
            data.to_csv(f"{filename}.csv", index=False)
            print(f"Data saved successfully as {filename}.csv")
            break
        elif answer == 'no':
            print("Data will not be saved.")
            break
        else:
            print("Invalid response. Please type 'yes' or 'no'.")


# Loading the CSV file with Olympics data
df = pd.read_csv('olympics2024.csv')

# Allowing the display of all rows in large outputs
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print('Welcome to the 2024 Olympics Medals Viewer!\n')

# Main menu loop for the program
while True:
    print('Select the viewing method:')
    print('1- Country Ranking')
    print('2- All sports from one country')
    print('3- All athletes from one sport')
    print('4- Exit')
    answer = input()

    if answer == '1':
        country_rank()  # Display country rankings
    elif answer == '2':
        sports_country()  # Display sports per country
    elif answer == '3':
        athletes_sport()  # Display athletes for a sport
    elif answer == '4':
        break  # Exit the program
    else:
        print('Invalid choice. Please select a valid method (1, 2, 3) or 4 to exit.')  # Handling invalid input
