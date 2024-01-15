def store(list_product, product):
    if product in list_product:
        index = list_product.index(product)
        print(index)
    else:
        print("Продукт отсутствует")


list_product = ["Чипи", "Чапа", "Дуби", "Даба", "Бум", "Буум"]
product = "Чапа"
store(list_product, product)
