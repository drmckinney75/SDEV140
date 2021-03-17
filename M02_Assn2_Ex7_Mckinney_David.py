#David Ryan McKinney
#SDEV140
#M02_Assn2_Ex7
#1/26/21
#Program written to display a strange salary arrangement
#days (int) number of days for doubling salary arrangement
#salary (float) daily salary in range
#total (float) running total of salary calculations

print('Hello User. Conned your employer into a Doubling Salary Arrangement?')
print('Allow DRM Enterprises to help you calculate your wealth!')
days = int(input('Enter the number of days: '))
print('Day\t\t', 'Salary')
print('-' * 25)
total = 0
for i in range(1, days + 1):
    salary = 0.01 * 2 ** (i -1)
    print(format(i, '3.0f'), '\t\t$', format(salary, '8.2f'))
    total += salary
print('Total salary $', (format(total, '.2f')))