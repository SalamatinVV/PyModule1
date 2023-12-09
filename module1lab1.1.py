list_ = [8, 10, 15, 7, 92, 1, None, 74, 42, 10, 24]
for i in range(len(list_)) :
    if list_[i] == None :
        list_[i] = 0
        list_[i] = sum(list_) / len(list_)
print(list_)
