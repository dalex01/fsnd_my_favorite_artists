import media
import index_template
import spotipy

artists_list = {
	'Rammstein': 'band',
#	'Infected Mashroom': 'band',
#	'Scorpions': 'band',
	'Hans Zimmer': 'singer',
#	'Pink Floyd': 'band',
#	'Red Hot Chili Peppers': 'band',
#	'Therion': 'band',
#	'Apocalyptica': 'band',
#	'Anathema': 'band',
#	'Tiamat': 'band',
#	'Moonspell': 'band',
#	'Funker Vogt': 'band',
#	'Fort Minor': 'band',
#	'Amorphis': 'band',
#	'Blind Guardian': 'band',
#	'Disturbed': 'band',
#	'Metallica': 'band',
#	'Helloween': 'band',
#	'Iron Maiden': 'band',
	'Sabaton': 'band'}

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
			for album in alb['items']:
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
		print(artist)
		artists.append(artist)
	return artists

print(fillArtists(artists_list))
#index_template.open_artists_page(fillArtists(artists_list))