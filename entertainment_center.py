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

	for name, tp in artists_list.items():
		results = spotify.search(q='artist:' + name, type='artist')
		items = results['artists']['items']
		artist = None
		if len(items) > 0:
			art = items[0]
			uri = art['uri']
			alb = spotify.artist_albums(uri, album_type='album')
			albums = []
			albums_names = []
			for album in alb['items']:
				if album['name'] not in albums_names:
					albums_names.append(album['name'])
					alb_uri = album['uri']
					sng = spotify.album_tracks(alb_uri)
					songs = []
					for song in sng['items']:
						songs.append(media.Song(song['uri'], song['name'], song['duration_ms'], song['preview_url'], song['external_urls']['spotify']))
					albums.append(media.Album(alb_uri, album['name'], songs, album['images'][0]['url'], album['external_urls']['spotify']))
			if(tp == "band"):
				artist = media.Band(uri, art['name'], albums, art['external_urls']['spotify'])
			elif(tp == "singer"):
				artist = media.Singer(uri, art['name'], albums, art['external_urls']['spotify'])
		#print(artist)
		artists.append(artist)
	return artists

#print(fillArtists(artists_list)[0].name)
index_template.open_artists_page(fillArtists(artists_list))