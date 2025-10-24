job_years = 1
salary = 90000
message = 'Your premium ratio {}, and your new salary {}'


if job_years >=3:
    coef = 0.30
elif job_years >=1 and job_years <=3:
    coef = 0.20
else:
    coef = 0.10

salary = salary + salary * coef
print(message.format(coef, salary))123