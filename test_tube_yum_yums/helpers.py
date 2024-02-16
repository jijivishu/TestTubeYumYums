'''
This file contains helper functions for analysing test result(s) based on it's ranges and return analysis summary with recommended food items(optional).
'''

# Python-based imports
import sys
import requests
from decimal import Decimal

# Internal Imports
from test_tube_yum_yums.api_codes import nutrients
from test_tube_yum_yums.cbc_analyser import extract_nutrient_variation_by_cbc
from test_tube_yum_yums.food_codes import nutrients as code_of_nutrients
from yum_yums.models import FoodItem


# Called before rendering the landing page appropriately
def analyse(cbc, cbc_low, cbc_high, vitMin, vitMin_low, vitMin_high):
    '''
    Takes as input the CBC and/or Vitamin value(object) to be analysed, 
    alongwith their lower and upper ranges(objects). 

    Returns a dictionary containing the following fields: 
    'analysis': Summarises the analysis based on user's report. 
    'foods' (optional) : List of food items(dictionaries) based on the analysis.
    '''


    # Empty list to contain list of recommended food items
    recommended_food_list = []

    # Empty lists to contain list of deficient and exceeding nutrients.
    low_nutrients = []
    high_nutrients = []

    # Empty variable to contain message summing up the analysis.
    analysis_message = None

    # Based on received values, assign deficient and excess nutrients to the list of low and high nutrients.
    if vitMin:
        # For vitamin and minerals, the name of parameters directly represent nutrients.
        vitMin_oor_parameters = out_of_range_filter(vitMin, vitMin_low, vitMin_high)
        low_nutrients += vitMin_oor_parameters['low']
        high_nutrients += vitMin_oor_parameters['high']
    if cbc:
        # For Common Blood Test(CBC), the name of parameters do not represent nutrients directly. 
        cbc_oor_parameters = out_of_range_filter(cbc, cbc_low, cbc_high)
        low_parameters = cbc_oor_parameters['low']
        high_parameters = cbc_oor_parameters['high']

        # Analyse low and high parameters collectively to access nutrient's excess and deficiency.
        cbc_oor_parameters = extract_nutrient_variation_by_cbc(low_parameters, high_parameters)
        low = cbc_oor_parameters['low_nutrients']
        high = cbc_oor_parameters['high_nutrients']
        analysis_message = cbc_oor_parameters['analysis_message']

        # Depending on the value of nutrients, assign them to their respective array.
        # In cases when the nutrient is already present classified by it's exact value, discard it's CBC based prediction.
        for item in low:
            if not (item in high_nutrients or item in low_nutrients):
                low_nutrients.append(item)

        for item in high:
            if not (item in high_nutrients or item in low_nutrients):
                high_nutrients.append(item)
    
    # Get food recommendations based on low and high parameters.
    recommended_food_list = recommend_food_items(low_nutrients, high_nutrients)

    # Response to be returned must contain summary of analysis to be displayed to the end user.
    response = {
        'analysis': analysis_message
    }

    # If any food recommendation is received, add it in the response. Otherwise, extend the analysis summary with an apology.
    if not recommended_food_list:
        response['analysis'] += 'Unfortunately, we have no food recommendations for you at the moment.'
    else:
        response['foods'] = recommended_food_list

    # Return respose(dictionary with key 'analysis' and 'foods')
    return response


# Called for filtering parameters based on range
def out_of_range_filter(report, min, max):
    '''
    Takes report object, upper range object and lower range object as input.


    Returns map with following keys:
    'low': Contains list of parameter names in report falling short of minimum value in range.
    'high': Contains list of parameter names in report exceeding maximum value in range.
    '''


    # Empty lists to contain list of lower and upper parameters.
    high_parameters = []
    low_parameters = []

    for parameter in report:
        # Skip id parameter
        if parameter == "id":
            continue
        
        # Assume that min and max will have no NoneType values, which they won't unless explicitly entered in the database.
        min_value = Decimal(min[parameter].strip(' "'))
        max_value = Decimal(max[parameter].strip(' "'))

        # Check for each parameter
        if report[parameter]:
            current_value = Decimal(report[parameter].strip(' "'))

            if current_value < min_value:
                low_parameters.append(parameter)
            elif current_value > max_value:
                high_parameters.append(parameter)
            else:
                pass
    
    return {"low": low_parameters, "high": high_parameters}


# Called for customising list of food items given the nutrient status 
def recommend_food_items(low, high):
    '''
    Takes as input, the list of low(deficient) and high(exceeding) nutrients 
    and returns a list of food items which contain excess and minimal amount of those nutrients respectively.
    '''

    # Load list of food items from database
    food_list = FoodItem.all_as_list_of_dict()

    # Make sure the list of food items is already imported.
    if not food_list:
        print("ERROR: Please make sure you've imported the food data. Run 'python manage.py load_food_data' in the terminal to import.")
        sys.exit(1)

    # Empty list to contain foods based on low and high nutrients
    recommend_food_list = []

    # Empty dictionaries to store key-value pairs of csv headings for a nutrient and their min/max value required to filter for recommending a food item.
    minimum_values = {}
    maximum_values = {}

    # Filter list of food items(dictionaries) based on the low(deficient) and high(exceeding) nutrients in the reports.
    for parameter in low:
        # For each low parameter, get the heading of column in the csv file (food data) corresponding to it.
        # Also, get the greater_than_usual(gtu) parameter which reflects what quantity of that parameter is considered high in 100grams of any food.
        parameter_code_data = code_of_nutrients[parameter]
        csv_heading = parameter_code_data['field_name']
        gtu = parameter_code_data['gtu']

        # Update corresponding dictionary for ease of filtering food items.
        minimum_values[csv_heading] = gtu

    for parameter in high:
        # For each high parameter, get the heading of column in the csv file (food_data) corresponding to it.
        # Also, get the lower_than_usual(ltu) parameter which reflects what quantity of that parameter is considered low in 100grams of any food.
        parameter_code_data = code_of_nutrients[parameter]
        csv_heading = parameter_code_data['field_name']
        ltu = parameter_code_data['ltu']

        # Update corresponding dictionary for ease of filtering food items.
        maximum_values[csv_heading] = ltu
        
    # Filter csv data based on those csv heading and ltu/htu values
    for food in food_list:

        # Optimum Nutrient count tells how many nutrients satisfy user's nutrient requirements compared to how many who don't.
        # It is used to display to the end user, how reliable a food item recommendation is.
        optimum_nutrient_count = 0

        # For every nutrient that was lower in test report, check every food to have adequate amount of that nutrient.
        for parameter_field_name, minimum_value in minimum_values.items():
            if food[parameter_field_name] > minimum_value:
                optimum_nutrient_count += 1
            else:
                optimum_nutrient_count -= 1

        # For every nutrient that was higher in test report, check every food to have minimal amount of that nutrient.
        for parameter_field_name, maximum_value in maximum_values.items():
            if food[parameter_field_name] < maximum_value:
                optimum_nutrient_count += 1
            else:
                optimum_nutrient_count -= 1

        # If the food has more nutrients that are in required range compared to the nutrients that aren't, recommend that food.
        if optimum_nutrient_count >= 0:
            # Based on total number of nutrients based on which the food was filtered,...
            # ...add a key containing reliability info within each food item(dictionary). 

            nutrients_in_consideration_count = len(minimum_values) + len(maximum_values)
            recommendation_reliability = 'Satisfactory'

            if optimum_nutrient_count == nutrients_in_consideration_count:
                recommendation_reliability = 'Excellent'
            elif optimum_nutrient_count > (nutrients_in_consideration_count // 2):
                recommendation_reliability = 'Good'
            
            # Add the food item to list of recommended food items.
            food["reliability"] = recommendation_reliability
            recommend_food_list.append(food)

    # Return the list of recommended food items
    return recommend_food_list


# NOTE: THIS FUNCTION IS NO LONGER IN USE
def fetch_food_from_api(low, high):
    '''
    THIS FUNCTION IS NO LONGER IN USE AFTER DEPRECATION OF NUTRITIONIX API'S V1 ENDPOINTS

    Takes as input, the list of low and high nutrients and returns list of food items based on results by Nutritionix API.
    '''


    # In body of the request, include which nutrients need to be accessed based on whether...
    # ...they surpass and subceed FDA recommended high and low nutrient contents respectively.
    full_nutrients = {}
    def format_nutrients():
        '''
        Populates full_nutrients dictionary with expected range of values of nutrients in demanded foods.
        '''

        nonlocal low, high, full_nutrients
        for item in low:
            if nutrients[item]:
                full_nutrients[nutrients[item]['code']] = {
                    'gte': nutrients[item]['gte']
                }
        for item in high:
            if [nutrients[item]]:
                full_nutrients[nutrients[item]['code']] = {
                    'lte': nutrients[item]['lte']
                }
    
    format_nutrients()

    # Fetch API credentials from environment variables
    api_id = 'YOUR_API_ID'
    api_key = 'YOUR_API_KEY'
    endpoint = 'YOUR_API_ENDPOINT'

    # Construct header as demanded
    header = {'Content-Type': 'application/json', "x-app-id": api_id, "x-app-key": api_key, "x-remote-user-id": "0"}

    # Construct body as demanded
    parameters = {
        "query": "",
        'detailed': True,
        'full_nutrients': full_nutrients
        # 'fields': 'item_name, nf_protein',
        # 'sort': 'nf_protein',
        # 'min_nf_protein': 10,
        # 'max_results': 10'
    }

    # Make POST request and wait for the response (Add async-await functionality)
    response = requests.post(endpoint, headers=header, json=parameters)

    # Empty list to populate with fetched food items
    food_list = []

    # Check for response and add food items if repose status reflects success.
    if response.status_code == 200:
        received = response.json()
        for food in received['branded']:
            food_list += food
        for food in received['common']:
            food_list += food
    else:
        print('No response')

    return food_list