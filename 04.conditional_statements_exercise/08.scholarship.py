from math import floor

income = float(input())
average_results = float(input())
minimum_salary = float(input())

social_scholarship = minimum_salary * 0.35 if income < minimum_salary and average_results > 4.5 else 0
excellent_results_scholarship = average_results * 25 if average_results >= 5.5 else 0

if(social_scholarship > excellent_results_scholarship):
    print(f'You get a Social scholarship {floor(social_scholarship)} BGN')
elif(excellent_results_scholarship > social_scholarship):
    print(f'You get a scholarship for excellent results {floor(excellent_results_scholarship)} BGN')
else:
    print('You cannot get a scholarship!')
