import pandas as pd

df = pd.read_csv("data_set/lesson_1_data.csv", encoding="cp1251", sep=";")


df = df.rename(
    columns={
        "Номер": "number",
        "Title": "title",
        "Дата создания": "creation_date",
        "Дата оплаты": "payment_date",
        "Статус": "status",
        "Заработано": "money",
        "Город": "city",
        "Платежная система": "payment_system",
    }
)

result = df.groupby("title", as_index=False).aggregate({"money": "sum"})

print(result)
