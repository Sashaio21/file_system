import os
import shutil

print(os.path.exists("read_file.py")) # существует ли файл

if os.path.exists("read_file.py"):
    print("файл существует")



# os.mkdir("reports/2026") # создаёт папку (директорию)


print(os.listdir("reports/2026")) # выводит список файлов и папок


path = "reports/2026"

print(os.path.isdir(path))
print(os.path.isfile(path))


shutil.rmtree(path)
# os.rmdir(r"reports\2026")