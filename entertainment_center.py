import media
import generate_html

# Choose movies to add to movielist
movielist = ["Birdman or (The Unexpected Virtue of Ignorance)",
             "American Sniper",
             "Boyhood",
             "The Grand Budapest Hotel",
             "The Imitation Game",
             "Selma",
             "The Theory of Everything",
             "Whiplash"]

# Initalise object for each movie in movielist
movies = [media.Movie(movie) for movie in movielist]

# Using list of objects, open the generated HTML page
generate_html.open_movies_page(movies)