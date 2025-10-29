worker = [
    ["Ivan", "Ivanov", 100000, 1],
    ["Petr", "Petrov", 150000, 2],
    ["Sidor", "Sidorov", 200000, 3],
]

status = [["Junior"], ["Middle"], ["Senior"]]
for user in worker:

    salary = user[2]
    level = user[3]

    if level == 1:
        status_result = status[0][0]
        coef = 1.1
    elif level == 2:
        status_result = status[1][0]
        coef = 1.2
    else:
        status_result = status[2][0]
        coef = 1.3

    final_salary = salary * coef

    print(
        f"{user[0]} {user[1]} is a {status_result} and his salary with coefficient {coef} is equal {final_salary:g} rub"
    )
