"""
Find new movies.
Two lists are compared:
1. The list of movies already in my collection (mine)
2. The list of movies in the library (theirs)
"""
import csv
import dataclasses
import json
from dataclasses import dataclass
from time import sleep  # Add this import at the top with other imports
from typing import Dict, Any
from typing import List

import requests
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    omdb_api_key: str = ""

    class Config:
        env_file = ".env"


@dataclass
class Rating:
    Source: str
    Value: str


@dataclass
class Movie:
    Title: str
    Year: str
    Rated: str
    Released: str
    Runtime: str
    Genre: str
    Director: str
    Writer: str
    Actors: str
    Plot: str
    Language: str
    Country: str
    Awards: str
    Poster: str
    Ratings: List[Rating]
    Metascore: str
    imdbRating: str
    imdbVotes: str
    imdbID: str
    Type: str
    DVD: str
    BoxOffice: str
    Production: str
    Website: str
    Response: str
    totalSeasons: str = ""
    Seasons: str = ""
    totalEpisodes: str = ""
    Episodes: str = ""


def fetch_movie_from_omdb(title: str, api_key: str) -> Dict[str, Any]:
    """
    Fetches movie data from the OMDb API by title.

    :param title: The movie title to search for.
    :param api_key: Your OMDb API key.
    :return: A dict of the JSON response.
    :raises ValueError: If OMDb returns an error response.
    :raises requests.HTTPError: On network/HTTP errors.
    """
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,  # title to search
        "apikey": api_key,  # your API key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # raise on 4xx/5xx
    data = response.json()

    if data.get("Response", "False") == "False":
        # OMDb signals error via Response: "False" plus an "Error" field
        raise ValueError(f"OMDb error: {data.get('Error', 'Unknown error')}")

    return data


def fetch_all_movies(csv_file: str, settings: Settings) -> List[Movie]:
    """
    Read titles from CSV file and fetch movie data for each title.

    :param csv_file: Path to the CSV file containing movie titles
    :param settings: Settings object containing the API key
    :return: List of Movie objects
    """
    movies = []

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            title = row[0]  # Assuming title is in the first column
            try:
                print(f"Fetching data for: {title}")
                data = fetch_movie_from_omdb(title, settings.omdb_api_key)
                ratings = [Rating(**r) for r in data.pop("Ratings")]
                movie = Movie(Ratings=ratings, **data)
                movies.append(movie)
                # Add a small delay to avoid hitting API rate limits
                sleep(0.5)
            except Exception as e:
                print(f"Error fetching data for {title}: {str(e)}")
                continue

    return movies


def read_movies_jsonl(jsonl_file: str) -> List[Movie]:
    movies = []
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            ratings = [Rating(**r) for r in data.pop("Ratings")]
            movie = Movie(Ratings=ratings, **data)
            movies.append(movie)
    return movies


def example1():
    json_str = '''{"Title":"The Boys from Brazil","Year":"1978","Rated":"R","Released":"06 Oct 1978","Runtime":"125 min","Genre":"Drama, Mystery, Sci-Fi","Director":"Franklin J. Schaffner","Writer":"Ira Levin, Heywood Gould","Actors":"Gregory Peck, Laurence Olivier, James Mason","Plot":"A Nazi hunter in Paraguay discovers a sinister and bizarre plot to rekindle the Third Reich.","Language":"English, Spanish","Country":"United Kingdom, United States","Awards":"Nominated for 3 Oscars. 2 wins & 13 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BMjI4ZTFjZGMtNjUyOS00Y2FiLTkwNWMtZGViNjgzODQ0NzIwXkEyXkFqcGc@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"7.0/10"},{"Source":"Rotten Tomatoes","Value":"70%"},{"Source":"Metacritic","Value":"40/100"}],"Metascore":"40","imdbRating":"7.0","imdbVotes":"32,238","imdbID":"tt0077269","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"N/A","Website":"N/A","Response":"True"}'''
    data = json.loads(json_str)
    ratings = [Rating(**r) for r in data.pop("Ratings")]
    movie = Movie(Ratings=ratings, **data)
    print(movie)


def example2():
    title = "The Boys from Brazil"
    data = fetch_movie_from_omdb(title, Settings().omdb_api_key)
    ratings = [Rating(**r) for r in data.pop("Ratings")]
    movie = Movie(Ratings=ratings, **data)
    print(movie)


def example3():
    settings = Settings()
    movies = fetch_all_movies('/Users/ericmelz/Data/code/synutil/source/movie_finder/data/theirs.csv', settings)
    # Print or process the results
    for movie in movies:
        print(f"\nTitle: {movie.Title}")
        print(f"Year: {movie.Year}")
        print(f"IMDB Rating: {movie.imdbRating}")

    # open the JSONL output file for writing
    out_path = '/Users/ericmelz/Data/code/synutil/source/movie_finder/data/theirs.jsonl'
    with open(out_path, 'w', encoding='utf-8') as out_f:
        for movie in movies:
            # convert dataclass (with nested Ratings) to plain dict
            movie_dict = dataclasses.asdict(movie)
            # write as a single JSON line
            out_f.write(json.dumps(movie_dict, ensure_ascii=False) + "\n")

    print(f"Wrote {len(movies)} records to {out_path}")


def example4():
    # TODO: read jsonl
    pass


if __name__ == '__main__':
    example4()
