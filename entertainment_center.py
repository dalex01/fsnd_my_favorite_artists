import media
import index_template
import spotipy

artists_list = {
#	'Rammstein': 'band',			# problem with encoding
	'Infected Mushroom': 'band',
	'Scorpions': 'band',
#	'Hans Zimmer': 'singer',		# problem with encoding
#	'Pink Floyd': 'band',			# problem with encoding
#	'Red Hot Chili Peppers': 'band',# problem with classes (hide/show logic)
#	'Therion': 'band',				# problem with encoding
	'Apocalyptica': 'band',
	'Anathema': 'band',
	'Tiamat': 'band',
	'Moonspell': 'band',
#	'Funker Vogt': 'band',			# problem with encoding
	'Fort Minor': 'band',
	'Amorphis': 'band',
	'Blind Guardian': 'band',
#	'Disturbed': 'band',			# problem with encoding
#	'Metallica': 'band',			# problem with classes (hide/show logic)
#	'Helloween': 'band',			# problem with encoding
#	'Sabaton': 'band',				# problem with encoding
	'Iron Maiden': 'band'}


def fillArtists(artists_list):
	artists = []
	spotify = spotipy.Spotify()

	# loop through artists list
	for name, tp in artists_list.items():
		# search particular artist via spotipy
		results = spotify.search(q='artist:' + name, type='artist')
		items = results['artists']['items']
		artist = None
		# if artist is found
		if len(items) > 0:
			art = items[0]
			uri = art['uri']
			# get list of artists albums via spotipy
			alb = spotify.artist_albums(uri, album_type='album')
			albums = []
			albums_names = []
			# loop through all artists albums
			for album in alb['items']:
				# if album with the same name was not processed earlier
				if album['name'] not in albums_names:
					albums_names.append(album['name'])
					alb_uri = album['uri']
					# get list of albums songs via spotipy
					sng = spotify.album_tracks(alb_uri)
					songs = []
					# loop through all albums songs
					for song in sng['items']:
						# fullfill songs list with songs from Spotify
						songs.append(media.Song(song['uri'], song['name'], song['duration_ms'], song['preview_url'], song['external_urls']['spotify']))
					# fullfill albums list with albums from Spotify
					albums.append(media.Album(alb_uri, album['name'], songs, album['images'][0]['url'], album['external_urls']['spotify']))
			# if artist is band create Band class
			if(tp == "band"):
				artist = media.Band(uri, art['name'], albums, art['external_urls']['spotify'])
			# if artist is singer create Singer class
			elif(tp == "singer"):
				artist = media.Singer(uri, art['name'], albums, art['external_urls']['spotify'])
		# fullfill artists list with artists from Spotify
		artists.append(artist)
	return artists

index_template.open_artists_page(fillArtists(artists_list))