''''
user_info = [['John', 'Lennon', '150000', '3'],['Ivan', 'Ivanov', '100000', '1'], ['Petr', 'Petrov', '125000', '2']]

['Petr', 'Petrov', '125000', '2']

for i in user_info:
    if i[1] == 'Lennon':
        print(i)
    else:
        print('no')



user_ages = [10, 18, 21, 35, 42, 27, 12, 16]

for i in user_ages:
    if i >= 18:
        print('Yes, I am an adult, I am {} years old.'.format(i))




 
users = [['Ivan', 'Ivanov', 100000, 2], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]

users.append(['Pavel', 'Pavlov', 300000, 5])

print(users[3])


'''

