# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:22:46 2020

@author: Lenssen
"""

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary = annual_salary / 12
for month in range(1,1000):
    current_savings += (current_savings * (0.04 / 12)) + monthly_salary *  portion_saved  
    if current_savings >= portion_down_payment:
        print('Number of months:',str(month))
        break
