'''
This file has been extended to load the food data from CSV and store in list of food items(dictionaries)
when the app is being initialized. This saves us from loading csv everytime, for each operation.

The loaction of csv is assigned to be same as manage.py file and it is named 'food_data.csv'.
To modify it, visit settings.py

This file also facilitates loading ranges of parameters when the migrations occur for the very first time for CBC and VitMin model.
'''


# Python-based imports
import sys
import csv
import re

# Django-based import
from django.apps import AppConfig
from django.conf import settings

# List instance to store list of every food item(dictionary) globally at the app launch.
food_list = list()
food_data_path = settings.FOOD_DATA_PATH

# Convert headings of csv databse to valid snake_case
def modify_to_snake(heading):
    '''
    Converts strings into valid snake case with the help of regex
    '''

    # Replace anything except a-z, A-Z, 0-9 with an underscore. Also,
    heading = re.sub(r'[^a-zA-Z0-9]+', '_', heading)

    # If two underscores are consecutive, remove one

    # Remove leading and trailing underscores(if any) and return lower case
    return heading.lower().lstrip('_').rstrip('_')



class TesttubeyumyumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TestTubeYumYums'

    # When the app is being initialized, load the food data from CSV and store in list of food items(dictionaries) 
    def ready(self) -> None:
        # If migrations are being made for the first time, load ranges of parameters as well by connecting signals.
        import TestTubeYumYums.signals

        try:
            # Open the CSV file for food data.
            with open(food_data_path, 'r', newline='', encoding='utf-8-sig') as food_data_csv:
                # Read each food item from CSV file as a dictionary.
                food_data = csv.DictReader(food_data_csv)

                # Convert all headings to valid snake_case
                snake_headings = [modify_to_snake(headings) for headings in food_data.fieldnames]

                print(snake_headings)

                # Create dictionary with new keys(headings) and load csv
                food_data = csv.DictReader(food_data_csv, fieldnames=snake_headings)

                # Append each food item to list in the global variable food_list.
                for food in food_data:
                    # Convert values for numeric columns into float if they've floating point.
                    float_columns = [
                        'calories_in_kcal', 'total_fat_in_g', 'saturated_fat_in_g', 'trans_fat_in_g',
                        'cholesterol_in_mg', 'sodium_in_mg', 'carbohydrate_in_g', 'dietary_fiber_in_g',
                        'sugar_in_g', 'protein_in_g', 'calcium_in_mg', 'iron_in_mg', 'potassium_in_mcg',
                        'vitamin_a_in_mcg', 'vitamin_b1_in_mg', 'vitamin_b2_in_mg', 'vitamin_b3_in_mg',
                        'vitamin_b4_in_mg', 'vitamin_b5_in_mg', 'vitamin_b6_in_mg', 'vitamin_b9_in_mcg',
                        'vitamin_b12_in_mcg', 'vitamin_c_in_mg', 'vitamin_d_in_mcg', 'vitamin_e_in_mg',
                        'vitamin_k_in_mcg', 'phosphorus_in_mg', 'magnesium_in_mg', 'zinc_in_mg',
                        'copper_in_mg', 'recommended_portion_in_g'
                    ]

                    for column in float_columns:
                        value_of_current_parameter = food[column]

                        # Remove comma from longr values like 1,124 or 1,112.02
                        if ',' in value_of_current_parameter:
                            value_of_current_parameter = value_of_current_parameter.replace(',', '')
                        
                        # For values with no floating point, convert them to integer. Otherwise, convert them to float.
                        value_of_current_parameter = float(value_of_current_parameter)
                        food[column] = int(value_of_current_parameter) if value_of_current_parameter.is_integer() else value_of_current_parameter

                    food_list.append(food)

            # Notify end-user about the successful import.
            print('Food data from CSV has been loaded successfully :)')

        # If food_data.csv is absent, or some error occurs while loading data from csv to python, exit.
        except (ValueError, csv.Error) as e:
            print(f'ERROR => {e}')
            sys.exit("Error loading food database(csv). Make sure food_data.csv is present in main directory of your project(alongside manage.py)")
