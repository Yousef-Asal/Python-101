import pickle

with open('Assignment_1/books.pkl', 'rb') as f:
    books = pickle.load(f)
with open('Assignment_1/movies.pkl', 'rb') as fl:
    movies = pickle.load(fl)

# print(books)
# print(movies)

class media:
    def __init__(self, title, year, type):
        self.title = title
        self.year = year
        self.type = type

    def print_description(self):
        print(f"This {self.type} was created in {self.year} and its name is: {self.title}")

class book(media):
    def __init__(self, title, year, author , n_pages):
        super().__init__(title, year, 'book')
        self.author = author
        self.n_pages = n_pages

    def detailed_info(self):
        super().print_description()
        print(f"- Author: {self.author} \n- Number of pages: {self.n_pages}")

class movie(media):
    def __init__(self, title, year, director , runtime):
        super().__init__(title, year, 'movie')
        self.director = director
        self.runtime = runtime

    def detailed_info(self):
        super().print_description()
        self.hours = self.runtime // 60
        self.miutes = self.runtime % 60
        print(f"- Director: {self.director} \n- Runtime: {self.hours}h.{self.miutes}m")

for b in books:
    bk = book(b["title"], b["year"], b["author"],b["n_pages"])
    bk.detailed_info()

print("*"*50)

for m in movies:
    mv = movie(m["title"], m["year"], m["director"], m["runtime"])
    mv.detailed_info()
