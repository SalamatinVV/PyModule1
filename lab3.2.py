def find_common_participants(group1, group2):
    list_group1 = set(group1.split(","))
    list_group2 = set(group2.split(","))
    dict_result = list_group1.intersection(list_group2)
    list_result =[]
    for person in dict_result:
        list_result.append(person)
    list_result.sort()
    print(list_result)


group1 = "Ивановский,Даркаев,Дадаев,Поволяев,Касапов,Андреев,Куреленко"
group2 = "Даркаев,Кожевников,Поволяев,Дадаев,Иванов,Швед,Лангян"

find_common_participants(group1, group2)
