"""
Olympic Medal Data Processing - 2024

This script processes and transforms raw data from a text file, which was created by collecting data from the official
Olympic website (https://olympics.com/en/paris-2024/medals). It identifies countries, sports, and medal-winning athletes,
then stores this information in a CSV file for future analysis. To test and explore the generated data, you can run
`olympics.py`, which provides various options for viewing medal rankings and statistics.

Data collection:
- Countries: Identified based on lines containing the word "flag", as each country was listed with its respective flag
in the source data.
- Sports: Extracted by identifying rows that contained both a country name and an action (e.g., 'close the row'), with
the sport being the text between these markers.

The output is a CSV file ('olympics2024.csv') containing the following columns: Country, Sport, Modality - Athlete,
Gold, Silver, and Bronze.

Author: [Marcelo Carteri de Assumpção]
"""

import pandas as pd

# List of countries and sports involved in the Olympics

# List of countries participating in the Olympics.
# Countries were extracted from the raw data by identifying lines with the word "flag", which marked a country name.

countries = ['Albania', 'Algeria', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Belgium',
             'Botswana', 'Brazil', 'Bulgaria', 'Cabo Verde', 'Canada', 'Chile', 'Colombia', "Côte d'Ivoire", 'Croatia',
             'Cuba', 'Cyprus', 'Czechia', "Democratic People's Republic of Korea", 'Denmark', 'Dominica',
             'Dominican Republic', 'Ecuador', 'Egypt', 'Ethiopia', 'Fiji', 'France', 'Georgia', 'Germany',
             'Great Britain', 'Greece', 'Grenada', 'Guatemala', 'Hong Kong, China', 'Hungary', 'India', 'Indonesia',
             'Ireland', 'Islamic Republic of Iran', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
             'Kenya', 'Kosovo', 'Kyrgyzstan', 'Lithuania', 'Malaysia', 'Mexico', 'Mongolia', 'Morocco', 'Netherlands',
             'New Zealand', 'Norway', 'Pakistan', 'Panama', "People's Republic of China", 'Peru', 'Philippines',
             'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Refugee Olympic Team', 'Republic of Korea',
             'Republic of Moldova', 'Romania', 'Saint Lucia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia',
             'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Tajikistan', 'Thailand', 'Chinese Taipei', 'Tunisia',
             'Türkiye', 'Uganda', 'Ukraine', 'United States of America', 'Uzbekistan', 'Zambia']

# List of sports in which medals were won.
# Sports were identified by finding rows containing a country name and a closing marker (e.g., "close the row"),
# with the sport name located between these two.

sports = ['Artistic Gymnastics', 'Athletics', 'Badminton', 'Breaking', 'Diving', 'Equestrian', 'Fencing', 'Golf',
          'Judo', 'Modern Pentathlon', 'Sailing', 'Skateboarding', 'Sport Climbing', 'Swimming', 'Table Tennis',
          'Wrestling', 'Basketball', 'Boxing', 'Canoe Slalom', 'Canoe Sprint', 'Cycling BMX Freestyle',
          'Cycling BMX Racing', 'Cycling Road', 'Cycling Track', 'Marathon Swimming', 'Rowing', 'Shooting', 'Surfing',
          'Tennis', 'Water Polo', '3x3 Basketball', 'Archery', 'Cycling Mountain Bike', 'Football', 'Handball',
          'Rugby Sevens', 'Taekwondo', 'Triathlon', 'Volleyball', 'Artistic Swimming', 'Hockey',
          'Trampoline Gymnastics', 'Weightlifting', 'Rhythmic Gymnastics', 'Beach Volleyball']

# Initialize variables
expanded_data = []  # Stores processed data
country, sport, athlete_modality = None, None, []  # Variables to hold current values
gold, silver, bronze = 0, 0, 0  # Medal counters

# Read the input file containing Olympic data
with open('olympics2024_data.txt', 'r', encoding='utf-8') as file:
    array = [line.strip() for line in file.readlines()]  # Remove newline characters

# Process each line of the file
for line in array:
    if line in countries:  # If the line matches a country
        country = line
    elif line in sports:  # If the line matches a sport
        sport = line
    else:  # If it's not a country or sport, it might be medal or athlete information
        if (not line.isnumeric() and 'flag' not in line and ':' not in line and len(line) > 1):
            if line == 'Gold medal':  # Gold medal count
                gold, silver, bronze = 1, 0, 0
            elif line == 'Silver medal':  # Silver medal count
                gold, silver, bronze = 0, 1, 0
            elif line == 'Bronze medal':  # Bronze medal count
                gold, silver, bronze = 0, 0, 1
            else:
                athlete_modality.append(line)  # Collect athlete/modality info

    # If all required data is collected, append it to expanded_data
    if country and sport and athlete_modality and (gold or silver or bronze):
        athlete_modality_str = ' - '.join(athlete_modality)  # Join athlete and modality info
        expanded_data.append([country, sport, athlete_modality_str, gold, silver, bronze])  # Add the record
        gold, silver, bronze = 0, 0, 0  # Reset medal counters
        athlete_modality = []  # Reset athlete/modality list

# Create a DataFrame from the collected data
df = pd.DataFrame(expanded_data, columns=['Country', 'Sport', 'Modality - Athlete', 'Gold', 'Silver', 'Bronze'])

# Export the DataFrame to a CSV file
df.to_csv('olympics2024.csv', index=False)

print("Data successfully processed and saved to 'olympics2024.csv'.")
