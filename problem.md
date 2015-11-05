# Problem to solve

I have a list of favourite artists and songs. I want to be able to:
* store playlist of these songs in the app
* see artists albums and information about it
* TBD

# Suggested solution

* Classes diagram:
  * Artist
    * Singer (inheritance from Artist)
    * Band (inheritance from Artist)
  * Album
  * Songs

Classes diagram you can find [here](https://docs.google.com/presentation/d/1lCeJNrxXgXHp2ibShf6HDE9Za4iPSkm7es68OSq8m_c/edit?usp=sharing).

* Used API
  * Spotify (using python wrapper spotipy)

## Steps

1. List of artists will be created
2. For each artist all its albums will be downloaded using API
3. For each album list of songs will be downloaded using API
4. All received information will be displayed in web page using prepared html template

## Pseudocode

* Create Artist class that should store
  * name
  * list of albums
* Create Singer class that should store
  * borth date
  * death date (if applicable)
* Create Band class that should store
  * number of participants
  * their names
* Create Album class that should store
  * name
  * year of creation
  * list of songs
* Create Song class that should store
  * name
  * duration
* Create list of artists - singers or bands (will be hardcoded)
* Iterate through all artists and download artist's albums via API
* Iterate through all albums and download album's songs via API
* Create html template
* Display all into template and generate index.html page