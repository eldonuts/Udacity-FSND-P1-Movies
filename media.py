import webbrowser
import urllib2
import json

class Movie():
    def __init__(self, movie_title):
        self.title = movie_title

        try:
            #get json data from omdb for movie
            omdb_json = urllib2.urlopen('http://www.omdbapi.com/?t='+movie_title.replace(" ", "+")+'&y=&plot=full&r=json')
            omdb_data = json.load(omdb_json)

            self.storyline = omdb_data["Plot"]
            self.poster_image_url = omdb_data["Poster"]
            self.metascore = omdb_data["Metascore"]
            self.imdb_rating = omdb_data["imdbRating"]
            self.year = omdb_data["Year"]
            self.runtime = omdb_data["Runtime"]
            self.genre = omdb_data["Genre"]
            self.director = omdb_data["Director"]
            self.writer = omdb_data["Writer"]
            self.actors = omdb_data["Actors"]

            #get json data from youtube
            youtube_json = urllib2.urlopen('http://gdata.youtube.com/feeds/api/videos?q='+movie_title.replace(" ", "+")+'-trailer&start-index=1&max-results=1&v=2&alt=json&hd')
            youtube_data = json.load(youtube_json)

            self.trailer_youtube_id = youtube_data["feed"]["entry"][0]["media$group"]["yt$videoid"]["$t"]
            self.trailer_youtube_thumbnail = youtube_data["feed"]["entry"][0]["media$group"]["media$thumbnail"][1]["url"]
        except:
            raise Exception("Could not collect JSON data for "+movie_title)