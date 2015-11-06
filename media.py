class Artist():
    """TBD"""
    def __init__(self, id, name, albums = None, url = None):
        self.id = id
        self.name = name
        self.albums = albums
        self.url = url

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Singer(Artist):
    """TBD"""
    def __init__(self, id, name, albums = None, url = None, borth_date = None, death_date = None):
        Artist.__init__(self, id, name, albums, url)
        self.borth_date = borth_date
        self.death_date = death_date

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Albums: " + str(self.albums) + "\n" + \
               "Borth date: " + str(self.borth_date) + "\n" + \
               "Death date: " + str(self.death_date) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Band(Artist):
    """TBD"""
    def __init__(self, id, name, albums = None, url = None, participants = None):
        Artist.__init__(self, id, name, albums, url)
        self.num_of_participants = len(participants) if participants else None
        self.participants = participants

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Albums: " + str(self.albums) + "\n" + \
               "# of participants: " + str(self.num_of_participants) + "\n" + \
               "Participants: " + str(self.participants) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Album():
    """TBD"""
    def __init__(self, id, name, songs = None, cover = None, url = None):
        self.id = id
        self.name = name
        self.songs = songs
        self.cover = cover
        self.url = url

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Songs: " + str(self.songs) + "\n" + \
               "Cover: " + str(self.cover) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Song():
    """TBD"""
    def __init__(self, id, name, duration = None, preview = None, url = None):
        self.id = id
        self.name = name
        self.duration = duration
        self.preview = preview
        self.url = url

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Duration: " + str(self.duration) + "\n" + \
               "Preview: " + str(self.preview) + "\n" + \
               "Url: " + str(self.url) + "\n"
