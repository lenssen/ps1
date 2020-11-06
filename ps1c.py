# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:54:23 2020

@author: Lenssen
"""

down_payment = 0.25 * 1000000
current_savings = 0
starting_salary = int(input('Enter the starting salary: '))
low  = 0
high = 10000
ans = (high + low ) // 2
steps = 0
portion_saved = 0
Answer = ''
while(abs(down_payment - current_savings) >= 100):  
    current_savings = 0
    annual_salary = starting_salary
    for month in range(1,37):
        portion_saved = ans/10000
        monthly_salary = annual_salary / 12
        current_savings += (current_savings * (0.04 / 12)) + monthly_salary *  portion_saved  
        if month % 6 == 0:
            annual_salary += annual_salary * 0.07
    if current_savings < down_payment:
        low = ans
    else:
        high = ans    
    ans = (high + low ) // 2
    if ans <= 0 or ans >= 9999:
        Answer = 'No'
        break
    steps += 1    
if Answer == 'No':
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:',portion_saved)   
    print('Steps in bisection search:',steps)     