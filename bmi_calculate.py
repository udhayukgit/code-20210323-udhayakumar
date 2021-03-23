#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import json, sys 

# Bmi category list

bmi_list = [
    {
        'Bmi Category': 'Underweight',
        'Health Risk': 'Malnutrition risk',
        'Bmi Min': None,
        'Bmi Max': 18.4,
        },
    {
        'Bmi Category': 'NormalWeight',
        'Health Risk': 'Low risk',
        'Bmi Min': 18.5,
        'Bmi Max': 24.9,
        },
    {
        'Bmi Category': 'Overweight',
        'Health Risk': 'Enhanced risk',
        'Bmi Min': 25,
        'Bmi Max': 29.9,
        },
    {
        'Bmi Category': 'Moderately obese',
        'Health Risk': 'Medium risk',
        'Bmi Min': 30,
        'Bmi Max': 34.9,
        },
    {
        'Bmi Category': 'Severely obese',
        'Health Risk': 'High risk',
        'Bmi Min': 35,
        'Bmi Max': 39.9,
        },
    {
        'Bmi Category': 'Very severely Severely',
        'Health Risk': 'Very high risk',
        'Bmi Min': 40,
        'Bmi Max': None,
        },
    ]


# Calculate BMI
def bmi_calculator(file_path):

    df = pd.read_json(file_path, orient='records')

    # Bmi formula , BMI(kg/m2) = mass(kg) / height(m)**2 

    df['Bmi'] = df.apply(lambda x: round(x['WeightKg'] / (x['HeightCm'] / 100) ** 2, 2), axis=1)

    for bmi_range in bmi_list:

        if bmi_range['Bmi Min'] and bmi_range['Bmi Max']:
            df.loc[(df['Bmi'] >= bmi_range['Bmi Min']) & (df['Bmi'] <= bmi_range['Bmi Max']), ['Bmi Category', 'Health Risk']] = (bmi_range['Bmi Category'], bmi_range['Health Risk'])
        elif bmi_range['Bmi Min']:
            df.loc[df['Bmi'] >= bmi_range['Bmi Min'], ['Bmi Category', 'Health Risk']] = (bmi_range['Bmi Category'], bmi_range['Health Risk'])
        elif bmi_range['Bmi Max']:
            df.loc[df['Bmi'] <= bmi_range['Bmi Max'], ['Bmi Category', 'Health Risk']] = (bmi_range['Bmi Category'], bmi_range['Health Risk'])

    satistics = df['Bmi Category'].value_counts()    

    # Convert to Csv

    df.to_csv('Bmi_csv_output.csv')

    # Convert to Json

    df.to_json('Bmi_json_output.json',orient='records')

    #Statistics
    satistics.to_csv('Bmi_statistics.csv')

if __name__ == '__main__':
    # Json File Path

    #file_path = 'bmi_one_lakh_data.json'
    file_path = sys.argv[1]

    bmi_calculator(file_path)
