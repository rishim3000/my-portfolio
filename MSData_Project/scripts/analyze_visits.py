import pandas as pd
import numpy as np
import random
import math

def analysis_csv(filename, output):

    df = pd.read_csv(filename)

    df = df.dropna() #drop any missing values
    df = df.drop_duplicates() #drop any duplicates

    df['visit_date'] = pd.to_datetime(df['visit_date']) #converted visit_date col to datetime

    df['walking_speed'] = df['walking_speed'].astype(float)

    df.sort_values(by=['patient_id', 'visit_date'])#sort by patient_id and visit_date

    with open('insurance.lst', 'r') as file:
        words = [line.strip() for line in file.readlines()] #read each word of lst file


    pt_unique  = df['patient_id'].unique() # find unique patient_id vals

    insurance_assignment = pd.DataFrame({
        'patient_id': pt_unique,
        'insurance_type': np.random.choice(words, size=len(pt_unique), replace = True) #assign random insurance type to each patient id
    })

    df = df.merge(insurance_assignment, on='patient_id', how='left') #merge back into original dataset  

    def assign_visit_cost(i): #assign visit cost values based on insurance type
        if i == 'Basic':
            return 150
        elif i == 'Premium':
            return 100
        else:
            return 50
    df['visit_cost'] = df['insurance_type'].apply(assign_visit_cost) #create new col for visit costs
    
    df['visit_cost'] = df['visit_cost'] + np.random.normal(0,5, len(df)) #introduced some variation by adding a number with specified ranges

    df['visit_cost'] = df['visit_cost'].round(2) #round to 2 decimal places

    def age_category(age): #age categories
        if age < 25:
            return 'young adult'
        elif 25 <= age < 50:
            return 'middle aged'
        else:
            return 'elderly'
    df['age_category'] = df['age'].apply(age_category)
    
    walking_speed_education = df.groupby('education_level')['walking_speed'].mean()
    print(f"mean walking speed by {walking_speed_education}")

    cost_by_insurance = df.groupby('insurance_type')['visit_cost'].mean()
    print(f"mean visit cost by {cost_by_insurance}")

    walking_speed_age = df.groupby('age_category')['walking_speed'].mean()
    print(f"mean walking speed by {walking_speed_age}")



    df.to_csv(output, index = False) #write changes to new CSV file 
    
    





analysis_csv('ms_data.csv', 'ms_data_analyzed.csv')


