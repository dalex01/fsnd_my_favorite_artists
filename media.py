class Artist():
    """TBD"""
    def __init__(self, name, albums):
        self.name = name
        self.albums = albums


class Singer(Artist):
    """TBD"""
    def __init__(self, name, albums, borth_date, death_date = None):
        Artist.__init__(self, name, albums)
        self.borth_date = borth_date
        self.death_date = death_date

class Band(Artist):
    """TBD"""
    def __init__(self, name, albums, participants):
        Artist.__init__(self, name, albums)
        self.num_of_participants = len(participants)
        self.participants = participants

class Album():
    """TBD"""
    def __init__(self, name, year, songs, cover):
        self.name = name
        self.year = year
        self.songs = songs
        self.cover = cover

class Song():
    """TBD"""
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
