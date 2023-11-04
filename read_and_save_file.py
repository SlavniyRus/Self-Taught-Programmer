# Чтение файла
with open("test.txt", "r") as f:
    print(f.read())

# Сохранение содержимого файла в списке
my_list = []

with open("test.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
