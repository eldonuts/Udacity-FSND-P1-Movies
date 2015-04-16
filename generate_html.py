import webbrowser
import os

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>2015 Oscar Best Film Nominees</title>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1&controls=0&showinfo=0';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
    <body>
        <!-- Trailer Video Modal -->
        <div class="modal" id="trailer">
            <div class="modal-dialog">
                <div class="modal-content">
                    <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
                    <div class="scale-media" id="trailer-video-container">
                    </div>
                 </div>
            </div>
        </div>
    
        <!-- Main Page Content -->
        <div class="container">
            <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="container">
                    <div class="navbar-header">
                        <a class="navbar-brand" href="#">2015 Oscar Best Film Nominees</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="container">
            <ul class="list-group">
                {movie_tiles}
            </ul>
        </div>
    </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="panel panel-default">
    <div class="panel-heading">
        <center><b>{movie_title}</b></center>
    </div>
    <div class="panel-body">
        <div class="row">
            <div class="col-md-3">
                <img src="{poster_image_url}" class="img-rounded" width="261">
                    <div class="youtube-box movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                        <div class="img-overlay">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-youtube-play"></i>
                                </span>
                            </div>
                            <img src="{trailer_youtube_thumbnail}" class="img-rounded" width="261">
                    </div>
            </div>
            <div class="col-md-9">
                <p><b>{year} - {genre}</b></p>
                <p>{storyline}</p>
                <p><i class="fa fa-bullhorn fa-sm"></i><b> Director:</b> {director}</p>
                <p><i class="fa fa-pencil fa-sm"></i><b> Writer:</b> {writer}</p>
                <p><i class="fa fa-users fa-sm"></i><b> Actors:</b> {actors}</p>
                <p><i class="fa fa-film fa-sm"></i><b> Runtime:</b> {runtime}</p>
                <p><i class="fa fa-star fa-sm"></i><b> IMDB Score:</b> {imdb_rating}</p>
                <p><i class="fa fa-star fa-sm"></i><b> Metacritic Score:</b> {metascore}</p>
            </div>
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title.encode('utf-8'),
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = movie.trailer_youtube_id,
            storyline = movie.storyline.encode('utf-8'),
            imdb_rating = movie.imdb_rating,
            runtime = movie.runtime,
            trailer_youtube_thumbnail = movie.trailer_youtube_thumbnail,
            metascore = movie.metascore,
            genre = movie.genre.encode('utf-8'),
            year = movie.year,
            director = movie.director.encode('utf-8'),
            writer = movie.writer.encode('utf-8'),
            actors = movie.actors.encode('utf-8')
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('oscars_2015.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible