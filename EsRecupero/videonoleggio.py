class Movie:

    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director
        self.is_rented: bool = False

    def rent(self) -> None:

        if self.is_rented:
            print(f"Il film {self.title} è già noleggiato")
        
        else:
            self.is_rented = True


    def return_movie(self) -> None:

        if self.is_rented == False:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente")

        else:
            self.is_rented = False

class Customer:
    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id: str = customer_id
        self.name: str = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:

        if movie in self.rented_movies:
            print(f"Il film {movie.title} è già stato noleggiato")

        else:
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie) -> None:

        if movie not in self.rented_movies:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente")

        else:
            movie.return_movie()
            self.rented_movies.remove(movie)

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie] = None, customers: dict[str, Customer] = None) -> None:

        self.movies: dict[str, Movie] = movies if movies is not None else {}
        self.customers: dict[str, Customer] = customers if customers is not None else {}

    def add_movie(self, movie_id: str, title: str, director: str) -> None:

        if movie_id in self.movies:
            print(f"Il film con ID {movie_id} esiste già")

        else:
            movie: Movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie

    def register_customer(self, customer_id: str, name: str) -> None:

        if customer_id in self.customers:
            print("Il cliente è già registrato")

        else:
            customer: Customer = Customer(customer_id, name)
            self.customers[customer_id] = customer

    def rent_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id not in self.customers or movie_id not in self.movies:
            print("cliente o film non presenti nel sistema")

        else:
            movie:Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)

    def return_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id not in self.customers or movie_id not in self.movies:
            print("cliente o film non presenti nel sistema")

        else:
            movie:Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)

    def get_rented_movies(self, customer_id) -> list[Movie]:

        if customer_id not in self.customers:
            print("Cliente non nel sistema")

        else:
            return self.customers[customer_id].rented_movies
        
if __name__ == "__main__":

    bb:VideoRentalStore = VideoRentalStore()