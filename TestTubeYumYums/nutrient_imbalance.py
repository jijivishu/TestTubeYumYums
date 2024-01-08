'''
This file contains info about what type of parameter deviation can point towards which kind of nutrient imbalance.
__low__deviation suggests list of low nutrients due to followed deviation of parameters, whereas __high__deviation suggests 
list of low nutrients due to folowed deviation of parameters.
'''

__low__RBC_count_high = ['B9', 'Fe', 'B12', 'Cu', 'A', 'C', 'E']
__low__RDW_high_MCV_high = ['B9', 'B12']
__low__RDW_high_MCV_low_MCHC_high = ['Ca', 'D']
__low__RDW_high_MCV_low_MCHC_low = ['Fe', 'C']
__low__RDW_low_MCV_high_MCHC_high = ['Carb', 'Fat', 'B', 'D']
__low__RDW_low_MCV_high_MCHC_low =  ['B9']
__low__RDW_low_MCV_low_MCHC_high = ['Ca', 'D']
__low__RDW_low_MCV_low_MCHC_low = ['Fe', 'B', 'C']
__low__RDW_low_MCV_normal_MCHC_high = ['Fe', 'B12', 'B9', 'C']
__low__RDW_low_MCV_normal_MCHC_low = ['Fe', 'B12', 'B9']
__low__Hb_low =  ['Fe', 'C']

__high__RDW_high_MCV_low_MCHC_high = ['Fe', 'C']
__high__RDW_low_MCV_high_MCHC_high = ['Na']
__high__RDW_low_MCV_low_MCHC_high = ['Fe', 'C']