import csv
import json


def csv_to_json(csv_file, delimiter=',', newline='\n'):
    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file, delimiter=delimiter, lineterminator=newline)
            data_list = [row for row in csv_reader]
            json_data = json.dumps(data_list, indent=4)
            print(json_data)
            return json_data

    except FileNotFoundError:
        print(f"Файл '{csv_file}' не найден.")
    except Exception:
        print(f"Имеется ошибка")


csv_file = '/csv_file.csv'
result = csv_to_json(csv_file)
