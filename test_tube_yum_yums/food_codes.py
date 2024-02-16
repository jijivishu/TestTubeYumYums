'''
This file contains a global dictionary which links each nutrient with it's:

'field_name': field name for that nutrient in FoodItem model, 
'ltu' and 'gtu': lower_than_usual(ltu) and greater_than_usual(gtu) value of that nutrient per 100g of a food, 
'unit': the unit in which values of those nutrient are dealt in.
'''

nutrients = {
    'A': {
        'field_name': 'vitamin_a',
        'ltu': 50,
        'gtu': 200,
        'unit': 'mcg'
    },
    'B1': {
        'field_name': 'vitamin_b1',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B2': {
        'field_name': 'vitamin_b2',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B3': {
        'field_name': 'vitamin_b3',
        'ltu': 1,
        'gtu': 5,
        'unit': 'mg'
    },
    'B4': {
        'field_name': 'vitamin_b4',
        'ltu': 1,
        'gtu': 5,
        'unit': 'mg'
    },
    'B5': {
        'field_name': 'vitamin_b5',
        'ltu': 1,
        'gtu': 1,
        'unit': 'mg'
    },
    'B6': {
        'field_name': 'vitamin_b6',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B9': {
        'field_name': 'vitamin_b9',
        'ltu': 50,
        'gtu': 100,
        'unit': 'mcg'
    },
    'B12': {
        'field_name': 'vitamin_b12',
        'ltu': 0.1,
        'gtu': 1,
        'unit': 'mcg'
    },
    'C': {
        'field_name': 'vitamin_c',
        'ltu': 10,
        'gtu': 50,
        'unit': 'mg'
    },
    'D': {
        'field_name': 'vitamin_d',
        'ltu': 0.25,
        'gtu': 1,
        'unit': 'mcg'
    },
    'E': {
        'field_name': 'vitamin_e',
        'ltu': 1,
        'gtu': 3,
        'unit': 'mg'
    },
    'K': {
        'field_name': 'vitamin_k',
        'ltu': 10,
        'gtu': 20,
        'unit': 'mcg'
    },
    'Ca': {
        'field_name': 'calcium',
        'ltu': 50,
        'gtu': 100,
        'unit': 'mg'
    },
    'P': {
        'field_name': 'phosphorus',
        'ltu': 50,
        'gtu': 150,
        'unit': 'mg'
    },
    'Mg': {
        'field_name': 'magnesium',
        'ltu': 15,
        'gtu': 30,
        'unit': 'mg'
    },
    'Zn': {
        'field_name': 'zinc',
        'ltu': 1,
        'gtu': 2,
        'unit': 'mg'
    },
    'Fe': {
        'field_name': 'iron',
        'ltu': 1,
        'gtu': 3,
        'unit': 'mg'
    },
    'Na': {
        'field_name': 'sodium',
        'ltu': 0.14,
        'gtu': 0.4,
        'unit': 'mg'
    },
    'Cu': {
        'field_name': 'copper',
        'ltu': 0.1,
        'gtu': 0.5,
        'unit': 'mg'
    },
    'Pottas': {
        'field_name': 'potassium',
        'ltu': 100,
        'gtu': 400,
        'unit': 'mcg'
    },
    'Carb': {
        'field_name': 'carbohydrate',
        'ltu': 10,
        'gtu': 25,
        'unit': 'gram'
    },
    'Fat': {
        'field_name': 'total_fat',
        'ltu': 3,
        'gtu': 20,
        'unit': 'gram'
    },
    'Prot': {
        'field_name': 'protein',
        'ltu': 3,
        'gtu': 10,
        'unit': 'gram'
    },
    'Cal': {
        'field_name': 'calories',
        'ltu': 50,
        'gtu': 200,
        'unit': 'Kcal'
    },
    'Chol': {
        'field_name': 'cholesterol',
        'ltu': 20,
        'gtu': 150,
        'unit': 'mg'
    },
    'Sugar': {
        'field_name': 'sugar',
        'ltu': 5,
        'gtu': 10,
        'unit': 'g'
    },
    'DF': {
        'field_name': 'dietary_fiber',
        'ltu': 2,
        'gtu': 5,
        'unit': 'g'
    },
}
