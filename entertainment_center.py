import media
import index_template

artists_list = [
	'Rammstein',
	'Infected Mashroom',
	'Scorpions',
	'Rob Daugan',
	'Pink Floyd',
	'Red Hot Chili Peppers',
	'Therion',
	'Apocalyptica',
	'Anathema',
	'Tiamat',
	'Moonspell',
	'Funker Vogt',
	'Fort Minor',
	'Amorphis',
	'Blind Guardian',
	'Disturbed',
	'Metallica',
	'Helloween',
	'Iron Maiden',
	'Sabaton']

def fillArtists(artists_list):
	artists = []
#	for artist in artists_list:
#		artists.push(class Artist)
	return artists

index_template.open_artists_page(fillArtists(artists_list))