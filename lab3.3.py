def count_letters(text):
    text = text.lower()
    unique_letters = set(text)
    text_dict = {}
    for symbol in unique_letters:
        if not symbol.isalpha():
            continue
        else:
            text_dict[symbol] = text.count(symbol)
    print(text_dict)
    return text_dict


def calculate_frequency(text_dict):
    total_count = sum(text_dict.values())
    print("Total:", total_count)
    for i in text_dict:
        text_dict[i] = round((text_dict[i] / total_count), 2)
    for key, value in text_dict.items():
        print(key, ":", value)


text = "ЧОТА ТАМ2 или чота3 там1 или Chota2 tam ili 4ota tam"
text_dict = count_letters(text)
calculate_frequency(text_dict)
