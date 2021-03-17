#David McKinney
#Cookie Calculations
#SDEV140 M01-Assn2-Ex10
#Program designed to calculate ingredient quantities, depending on desired batch size
#batchSize (int) amount of cookies desired 
#cookies (int) amount of cookies base recipe uses
#sugar (float) amount of sugar used in base recipe
#butter (float) amount of butter used in base recipe
#flour (float) amount of flour used in base recipe
#userSugar (float) amount of sugar in user batch
#userButter (float) amount of butter in user batch
#userFlour (float) amount of flour in user batch
print('Welcome to our cookie recipe scaler!')
print('No more trying to calculate in your head!')
print('Leave the work to me.')
#declaring variables used to calculate output
cookies = 48
sugar = 1.5
butter = 1
flour = 2.75
#prompt user for desired batch size
batchSize = int(input('How many cookies would you like to make?'))
#calculating batch ingredients from user input
userSugar = (sugar * batchSize) / cookies
userButter = (butter * batchSize) / cookies
userFlour = (flour * batchSize) / cookies
#Output of ingredients required for user defined batch size
print(f'Desired number of cookies: {batchSize}')
print(f'Required sugar: {userSugar:.2f} cups')
print(f'Required butter: {userButter:.2f} cups')
print(f'Required flour: {userFlour:.2f} cups')