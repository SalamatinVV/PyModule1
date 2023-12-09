users = ["name1", "name2", "name1", "name3", "name1", "name4", "name5", "name7", "name2", "name2",]

dict_ = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0,
}

unique_users = set(users)

dict_["Общее количество"] = len(users)
dict_["Уникальные посещения"] = len(unique_users)

print(dict_["Общее количество"])
print(dict_["Уникальные посещения"])