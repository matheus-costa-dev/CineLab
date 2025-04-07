from requests import get
from pandas import DataFrame
from os.path import join
from os import listdir, makedirs

class Starwars():
    def __init__(self, n_movie):
        self.n_movie = n_movie
        self.movie = None

    def get_movie(self):
        self.movie = get(f"https://swapi.dev/api/films/{self.n_movie}").json()
        return self.movie
    
    def get_movie_info(self):
        if not hasattr(self,"movie") or self.movie == None:
            self.get_movie()

        movie_info = { col: [data] for col, data in self.movie.items() if not isinstance(data, list) }
        return DataFrame(movie_info)
    
    def extract_data(self, field:str) -> list:
        if not hasattr(self,"movie") or self.movie == None:
            self.get_movie()

        my_list = []
        for url_field in self.movie[field]:
            res = get(url_field).json()
            my_list.append(res)
        
        return my_list

    def get_characters_by_movie(self):
        characters = self.extract_data("characters")
        return DataFrame(characters)

    def get_planets_by_movie(self):
        planets = self.extract_data("planets")
        return DataFrame(planets)
    
    def get_species_by_movie(self):
        species = self.extract_data("species")
        return DataFrame(species)
    
    def get_starships_by_movie(self):
        starships = self.extract_data("starships")
        return DataFrame(starships)
    
    def get_vehicles_by_movie(self):
        vehicles = self.extract_data("vehicles")
        return DataFrame(vehicles)
    
    def get_all(self):
        return {
            "movie_info": self.get_movie_info(),
            "characters":self.get_characters_by_movie(),
            "planets":self.get_planets_by_movie(),
            "species":self.get_species_by_movie(),
            "starships":self.get_starships_by_movie(),
            "vehicles":self.get_vehicles_by_movie(),
        }
    
    def export_all_to_csv(self):

        all_data = self.get_all()

        folder = "datasets"
        sub_folder = f"starwars_{sw.movie["episode_id"]}"
        
        if not folder in listdir():
            makedirs(folder)
        
        if not sub_folder in listdir(folder):
            makedirs(join(folder, sub_folder))

        for name, df in all_data.items():
            df.to_csv(join(folder, sub_folder,f"{name}.csv"))



# if __name__ == "__main__":
    # sw = Starwars(n_movie=1)
    # sw.export_all_to_csv()


