from json import load, dump
# w - режим перезаписи файла (старое содержимое удаляет)
# with open("data/new_data.txt", "w", encoding="utf-8") as file:
#     file.write("Привет мир\n")
#     file.write("Hello world")


# with open("result.txt", "w", encoding="utf-8") as file:
#     file.write("Новая запись\n")

def write_user_message(message):
    with open("data/result.txt", "w", encoding="utf-8") as file:
        file.write(f"Письмо от юзера: {message}")
    
    print("Сообщение добавлена")

def append_new_user():
    count_user = int(input("Сколько юзеров добавить "))

    with open("data/users.txt", "a", encoding="utf-8") as file:
        for i in range(count_user):
            name = input(f"Введите имя юзера  ")
            file.write(name + "\n")



def append_film(title, raiting):
    with open("data/movies.json", "r", encoding="utf-8") as file:
        movies_data = load(file)


    for movie in movies_data:
        if movie["title"] == title:
            print("Фильм уже добавлен")
            return

    movies_data.append({
        "title": title,
        "raiting": raiting
    })

    with open("data\movies.json", "w", encoding="utf-8") as file:
        dump(movies_data, file, indent=4)
    
