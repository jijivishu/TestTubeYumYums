'''
This file contains helper function to return nutrient variation based on low and high CBC parameters
'''


# Internal import for value based analysis
from test_tube_yum_yums import analysis_messages, nutrient_imbalance

# Extract which nutrient varies based on out of range parameters of CBC
def extract_nutrient_variation_by_cbc(low, high):
    '''
    Takes as input list of low and high CBC parameters(names). \n\n

    Returns dictionary containing the following three keys: \n
    'low_nutrients': Contains list of deficient nutrients.
    'high_nutrients': Contains list of exceeding nutrients.
    'analysis_message': Contains short message analysing the report.
    '''
    

    def organise():
        '''
        Sometimes, variation of one CBC parameter reflects excess of a nutrient 
        while the same of another parameter reflects deficiency of that nutrient, simultaneously. \n
        In such scenarios, deficiency is generally overshadowed by excess unless we have the exact value 
        of that nutrient. \n
        This function serves the same purpose and removes a nutrient from deficient category in case of clash.
        It also converts analysis_message from list of string(s) to a clean and presentable string.
        '''
        nonlocal high_nutrients, low_nutrients, analysis_message
        high_nutrients = list(set(high_nutrients))
        low_nutrients = list(set(low_nutrients))
        for item in high_nutrients:
            if item in low_nutrients:
                low_nutrients.remove(item)

        if analysis_message:
            presentable_message = ''
            for message in analysis_message:
                presentable_message += message + ' '
            analysis_message = presentable_message

        
    
    high_nutrients = []
    analysis_message = []
    low_nutrients = []

    # Nutrient variation is extracted considering variation of each parameter and it's correlation with another parameters.
    if "RBC_count" in high:
        analysis_message.append(analysis_messages.high_RBC_count)
    elif "RBC_count" in low:
        analysis_message.append(analysis_messages.low_RBC_count)
        low_nutrients.extend(nutrient_imbalance.__low__RBC_count_high)
    
    if "RDW" in high:
        if "MCV" in high:
            low_nutrients = nutrient_imbalance.__low__RDW_high_MCV_high
            if "MCHC" in high:
                analysis_message.append(analysis_messages.RDW_high_MCV_high_MCHC_high)
            elif "MCHC" in low:
                analysis_message.append(analysis_messages.RDW_high_MCV_high_MCHC_low)
        elif "MCV" in low:
            if "MCHC" in high:
                analysis_message.append(analysis_messages.RDW_high_MCV_low_MCHC_high)
                high_nutrients = nutrient_imbalance.__high__RDW_high_MCV_low_MCHC_high
                low_nutrients = nutrient_imbalance.__low__RDW_high_MCV_low_MCHC_high
            elif "MCHC" in low:
                analysis_message.append(analysis_messages.RDW_high_MCV_low_MCHC_low)
                low_nutrients = nutrient_imbalance.__low__RDW_high_MCV_low_MCHC_low
    else:
        if "MCV" in high:
            if "MCHC" in high:
                analysis_message.append(analysis_messages.RDW_low_MCV_high_MCHC_high)
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_high_MCHC_high
                high_nutrients = nutrient_imbalance.__high__RDW_low_MCV_high_MCHC_high
            elif "MCHC" in low:
                analysis_message.append(analysis_messages.RDW_low_MCV_high_MCHC_low)
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_high_MCHC_low
        elif "MCV" in low:
            if "MCHC" in high:
                analysis_message.append(analysis_messages.RDW_low_MCV_low_MCHC_high)
                high_nutrients = nutrient_imbalance.__high__RDW_low_MCV_low_MCHC_high
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_low_MCHC_high
            elif "MCHC" in low:
                analysis_message.append(analysis_messages.RDW_low_MCV_low_MCHC_low)
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_low_MCHC_low
        else:
            if "MCHC" in high:
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_normal_MCHC_high
                if "platelets" in low:
                    analysis_message.append(analysis_messages.RDW_low_MCV_normal_MCHC_high_platelets_low)
                else:
                    analysis_message.append(analysis_messages.RDW_low_MCV_normal_MCHC_high_platelets_normal)
            elif "MCHC" in low:
                analysis_message.append(analysis_messages.RDW_low_MCV_normal_MCHC_low)
                low_nutrients = nutrient_imbalance.__low__RDW_low_MCV_normal_MCHC_low

    if "TLC" in low:
        analysis_message.append(analysis_messages.TLC_high)
    elif "TLC" in high:
        analysis_message.append(analysis_messages.TLC_low)

    if "DLC_E" in high:
        analysis_message.append(analysis_messages.DLC_E_high)
    if "DLC_L" in high:
        analysis_message.append(analysis_messages.DLC_L_high)
    elif "DLC_B" in high:
        analysis_message.append(analysis_messages.DLC_B_high)
    elif "DLC_N" or "DLC_M" in high:
        analysis_message.append(analysis_messages.DLC_N_or_M_high)

    if "platelets" in high:
        if "MPV" in high:
            analysis_message.append(analysis_messages.platelets_high_MPV_high)
        elif "MPV" in low:
            analysis_message.append(analysis_messages.platelets_high_MPV_low)
        else:
            analysis_message.append(analysis_messages.platelets_high_MPV_normal)
    elif "platelets" in low:
        if "MPV" in high:
            analysis_message.append(analysis_messages.platelets_low_MPV_high)
        elif "MPV" in low:
            analysis_message.append(analysis_messages.platelets_low_MPV_low)
        else:
            analysis_message.append(analysis_messages.platelets_low_MPV_normal)
    else:
        if "MPV" in high:
            analysis_message.append(analysis_messages.platelets_normal_MPV_high)
        elif "MPV" in low:
            analysis_message.append(analysis_messages.platelets_normal_MPV_low)

    if "Hb" in high:
        analysis_message.append(analysis_messages.Hb_high)
    elif "Hb" in low:
        analysis_message.append(analysis_messages.Hb_low)
        low_nutrients.extend(nutrient_imbalance.__low__Hb_low)

    # After nutrients are categorised on the basis of expected deficiency or excess, nutrients which somehow landed in both lists need to be managed.
    # Analysis message needs to be presented in a cleaner format (as a complete string instead of list of strings).
    organise()

    # Return map
    return {"high_nutrients": high_nutrients, "low_nutrients": low_nutrients, "analysis_message": analysis_message}
