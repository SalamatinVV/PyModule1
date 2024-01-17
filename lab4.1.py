import json


def weigth_score_sum(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        total_sum = sum(data_line['score'] * data_line['weight'] for data_line in data)
        round_sum = round(total_sum, 3)
        return round_sum
    except Exception:
        print(f'Имеется ошибка')


json_file = '.../file.json'
result = weigth_score_sum(json_file)
