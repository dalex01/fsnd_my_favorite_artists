### !!! Current content is just template taken from course movie project.
### !!! Should be refactored

import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Favorite Artists</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        h1 {
            font-size: 30px!important;
            margin-top: 0!important;
        }
        h2 {
            font-size: 24px!important;
        }
        h3 {
            font-size: 20px!important;
        }
        img {
            width: 90%;
        }
        .artist:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .album-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .album-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.artist', function (event) {
            $(".artist").each(function(){
                $('.' + $(this).text().replace(/\s+/g, '')).hide();
            });
            $('.' + $(this).text().replace(/\s+/g, '')).show();
        });
        $(document).on('click', '.album-tile', function (event) {
            $(".album-tile").each(function(){
                $('.' + $(this).text().replace(/[^a-zA-Z0-9]/g, '')).hide();
            });
            $('.' + $(this).text().replace(/[^a-zA-Z0-9]/g, '')).show();
        });
    </script>
</head>
'''

#main_page_style = '''
#    <style>
#'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><h1>My Favorite Artists</h1></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="col-md-2">
        {artists_list}
      </div>
      <div class="col-md-6 container">
        {albums_list}
      </div>
      <div class="col-md-4">
        {songs_list}
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
artist_tile_content = '''
<div>
    <h2 class="artist">{artist_title}</h2>
</div>
'''

def create_artists_tiles_content(artists):
    # The HTML content for this section of the page
    content = ''
    for artist in artists:

        # Append the tile for the movie with its content filled in
        content += artist_tile_content.format(
            artist_title = artist.name
        )
    return content

# A single movie entry html template
album_tile_content = '''
<div class="col-md-6 text-center album-tile {album_class}" style="display:none">
    <img src="{poster_image_url}">
    <h3>{album_title}</h3>
</div>
'''

def create_albums_tiles_content(artists):
    # The HTML content for this section of the page
    content = ''
    for artist in artists:
        for album in artist.albums:
            # Append the tile for the movie with its content filled in
            content += album_tile_content.format(
                album_title = album.name,
                poster_image_url = album.cover,
                album_class = artist.name.replace(" ", "")
            )
    return content

# A single movie entry html template
song_tile_content = '''
<div class="{song_class}" style="display:none">
    <h4><a href="{song_url}">{song_title}</a></h4>
    <audio controls name="media">
        <source src="{song_preview}" type="audio/mpeg">
    </audio>
</div>
'''

def create_songs_tiles_content(artists):
    # The HTML content for this section of the page
    content = ''
    for artist in artists:
        for album in artist.albums:
            for song in album.songs:
                # Append the tile for the movie with its content filled in
                content += song_tile_content.format(
                    song_title = song.name,
                    song_preview = song.preview,
                    song_url = song.url,
                    song_class = re.sub('[^a-zA-Z0-9]', "", album.name)
                )
    return content

def open_artists_page(artists):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        artists_list = create_artists_tiles_content(artists),
        albums_list = create_albums_tiles_content(artists),
        songs_list = create_songs_tiles_content(artists))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)