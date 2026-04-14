
def search_user(user):
    with open("data/users.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        for number ,line in enumerate(lines, start=1):
            if user == line.strip():
                return number




def search_films():
    with open("data/movies.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        for index, line in enumerate(lines, start=1):

            movie_data = line.split(",")
            movie = movie_data[0].strip()
            raiting = movie_data[1].strip()
            print(movie, "рейтинг:",  raiting)

