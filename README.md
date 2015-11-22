# My Popular Artists App

This app was created as [Udacity Programming Foundations with Python]() final project development.
[Here](https://github.com/dalex01/fsnd_my_favorite_artists/blob/master/problem.md) you can find detailed description of the problem solved in this app.

## Requirements

Project was reviewed according to this [rubric](https://docs.google.com/document/d/1xgMJ71VyFGxjEhz-_KHswSnoCx9Vge7VykDH05bsny0/pub?embedded=true).

## How to use

* To see this project on your PC you should just clone repository with command `git clone https://github.com/dalex01/fsnd_my_favorite_artists.git` and start index.html file.
* Or [click](dalex01.github.io/fsnd_my_favorite_artists)

Python 3 should be used to run this project

## Features

App shows my favorite artists, their albums and songs in albums. For each song you can listen some preview fragment or go to Spotify site to listen full song.

## APIs used

1. Spotify API (via spotipy python library)

## Known Problems (to be corrected)

1. Encoding problem with some composition
2. Class problem if name of artist and name of one of its album is the same
3. List of songs should be cleared when new artist is chosen but its album is not chosen yet

## How to make your own App

1. Download project or clone it via `git clone https://github.com/dalex01/fsnd_my_favorite_artists.git`
2. Correct list of you favorite artists in `entertainment_center.py` file
3. Run `python entertainment_center.py` to generate your own index.html file (python 3 should be installed in your system and path to it should be mentioned in PATH variable)