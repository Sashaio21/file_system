from write_file import *
from read_file import *
import os



name_dir = input("Введите название папки   ")
name_file = input("Введите название файла   ")

if name_dir not in os.listdir("."):
    os.mkdir(name_dir)   

with open(name_dir + "/" + name_file, "a", encoding="utf-8") as file:
    pass 


# with open(name_dir + "/" + name_file, "a", encoding="utf-8") as file:
#     pass



# write_user_message("Привет пайтон")
# append_new_user()

# search_name = input("Какого юзера найти")
# print(f"Пользователь {search_name} находится на {search_user(search_name)} строчке")
























# file = open("result.txt", "r", encoding="utf-8")
# for line in file:
#     print(line.strip()) 
# # content = file.read() чтение всего файла
# # print(content)



# print("hello\n")

# file.close()

# with open("data/new_data.txt", "r", encoding="utf-8") as file_data:
#     lines = file_data.readlines()
#     print(lines)
    


