class Artist():
    """This class provides a way to store artists related information"""
    def __init__(self, id, name, albums = None, url = None):
        self.id = id
        self.name = name
        self.albums = albums
        self.url = url                      # variable is not used currently

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Singer(Artist):
    """This class provides a way to store singer related information"""
    def __init__(self, id, name, albums = None, url = None, borth_date = None, death_date = None):
        Artist.__init__(self, id, name, albums, url)
        self.borth_date = borth_date        # variable is not used currently
        self.death_date = death_date        # variable is not used currently

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Albums: " + str(self.albums) + "\n" + \
               "Borth date: " + str(self.borth_date) + "\n" + \
               "Death date: " + str(self.death_date) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Band(Artist):
    """This class provides a way to store band related information"""
    def __init__(self, id, name, albums = None, url = None, participants = None):
        Artist.__init__(self, id, name, albums, url)
        self.num_of_participants = len(participants) if participants else None  # variable is not used currently
        self.participants = participants                                        # variable is not used currently

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Albums: " + str(self.albums) + "\n" + \
               "# of participants: " + str(self.num_of_participants) + "\n" + \
               "Participants: " + str(self.participants) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Album():
    """This class provides a way to store album related information"""
    def __init__(self, id, name, songs = None, cover = None, url = None):
        self.id = id
        self.name = name
        self.songs = songs
        self.cover = cover
        self.url = url      # variable is not used currently

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Songs: " + str(self.songs) + "\n" + \
               "Cover: " + str(self.cover) + "\n" + \
               "Url: " + str(self.url) + "\n"

class Song():
    """This class provides a way to store song related information"""
    def __init__(self, id, name, duration = None, preview = None, url = None):
        self.id = id
        self.name = name
        self.duration = duration    # variable is not used currently
        self.preview = preview
        self.url = url              # variable is not used currently

    def __str__(self):
        return "ID: " + str(self.id) + "\n" + \
               "Name: " + str(self.name) + "\n" + \
               "Duration: " + str(self.duration) + "\n" + \
               "Preview: " + str(self.preview) + "\n" + \
               "Url: " + str(self.url) + "\n"
