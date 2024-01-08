'''
This file contains a global dictionary which links each nutrient with it's: \n\n

'csv_key': heading in csv database, 
'ltu' and 'gtu': lower_than_usual(ltu) and greater_than_usual(gtu) value of that nutrient per 100g of a food, 
'unit': the unit in which values of those nutrient are dealt in.
'''


nutrients = {
    'A': {
        'csv_key': 'vitamin_a_in_mcg',
        'ltu': 50,
        'gtu': 200,
        'unit': 'mcg'
    },
    'B1': {
        'csv_key': 'vitamin_b1_in_mg',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B2': {
        'csv_key': 'vitamin_b2_in_mg',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B3': {
        'csv_key': 'vitamin_b3_in_mg',
        'ltu': 1,
        'gtu': 5,
        'unit': 'mg'
    },
    'B4': {
        'csv_key': 'vitamin_b4_in_mg',
        'ltu': 1,
        'gtu': 5,
        'unit': 'mg'
    },
    'B5': {
        'csv_key': 'vitamin_b5_in_mg',
        'ltu': 1,
        'gtu': 1,
        'unit': 'mg'
    },
    'B6': {
        'csv_key': 'vitamin_b6_in_mg',
        'ltu': 0.1,
        'gtu': 0.3,
        'unit': 'mg'
    },
    'B9': {
        'csv_key': 'vitamin_b9_in_mcg',
        'ltu': 50,
        'gtu': 100,
        'unit': 'mcg'
    },
    'B12': {
        'csv_key': 'vitamin_b12_in_mcg',
        'ltu': 0.1,
        'gtu': 1,
        'unit': 'mcg'
    },
    'C': {
        'csv_key': 'vitamin_c_in_mg',
        'ltu': 10,
        'gtu': 50,
        'unit': 'mg'
    },
    'D': {
        'csv_key': 'vitamin_d_in_mcg',
        'ltu': 0.25,
        'gtu': 1,
        'unit': 'mcg'
    },
    'E': {
        'csv_key': 'vitamin_e_in_mg',
        'ltu': 1,
        'gtu': 3,
        'unit': 'mg'
    },
    'K': {
        'csv_key': 'vitamin_k_in_mcg',
        'ltu': 10,
        'gtu': 20,
        'unit': 'mcg'
    },
    'Ca': {
        'csv_key': 'calcium_in_mg',
        'ltu': 50,
        'gtu': 100,
        'unit': 'mg'
    },
    'P': {
        'csv_key': 'phosphorus_in_mg',
        'ltu': 50,
        'gtu': 150,
        'unit': 'mg'
    },
    'Mg': {
        'csv_key': 'magnesium_in_mg',
        'ltu': 15,
        'gtu': 30,
        'unit': 'mg'
    },
    'Zn': {
        'csv_key': 'zinc_in_mg',
        'ltu': 1,
        'gtu': 2,
        'unit': 'mg'
    },
    'Fe': {
        'csv_key': 'iron_in_mg',
        'ltu': 1,
        'gtu': 3,
        'unit': 'mg'
    },
    'Na': {
        'csv_key': 'sodium_in_mg',
        'ltu': 0.14,
        'gtu': 0.4,
        'unit': 'mg'
    },
    'Cu': {
        'csv_key': 'copper_in_mg',
        'ltu': 0.1,
        'gtu': 0.5,
        'unit': 'mg'
    },
    'Pottas': {
        'csv_key': 'pottasium_in_mcg',
        'ltu': 100,
        'gtu': 400,
        'unit': 'mcg'
    },
    'Carb': {
        'csv_key': 'carbohydrate_in_g',
        'ltu': 10,
        'gtu': 25,
        'unit': 'gram'
    },
    'Fat': {
        'csv_key': 'total_fat_in_g',
        'ltu': 3,
        'gtu': 20,
        'unit': 'gram'
    },
    'Prot': {
        'csv_key': 'protein_in_g',
        'ltu': 3,
        'gtu': 10,
        'unit': 'gram'
    },
    'Cal': {
        'csv_key': 'calories_in_kcal',
        'ltu': 50,
        'gtu': 200,
        'unit': 'Kcal'
    },
    'Chol': {
        'csv_key': 'cholesterol_in_mg',
        'ltu': 20,
        'gtu': 150,
        'unit': 'mg'
    },
    'Sugar': {
        'csv_key': 'sugar_in_g',
        'ltu': 5,
        'gtu': 10,
        'unit': 'g'
    },
    'DF': {
        'csv_key': 'dietary_fiber_in_g',
        'ltu': 2,
        'gtu': 5,
        'unit': 'g'
    },
}
