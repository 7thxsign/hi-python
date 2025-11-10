import json
import csv
# txt_data = "hello world!"

# employees = ["John", "Doe", "Spongebob","Squidward"]
# employee = {  #for json
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30
# }
employees = [["Name", "Age", "Job"],
             ["Spongebob", 23, "Cook"],
             ["Patrick", 34, "Unemployed"],
             ["Squidward", 32, "Cashier"]
             ]

file_path = "C:/Users/Mithil/Documents/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print('CSV File Created')

except FileExistsError:
    print(f'File already exists')
finally:
    print(f'Operation took place.')