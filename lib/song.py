class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment song count
        self.add_song_to_count()

        # Track genres and artists
        self.genres.append(genre)
        self.artists.append(artist)

        # Update unique genres and artists
        self.add_to_genres()
        self.add_to_artists()

        # Update histograms
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        if cls.genres[-1] not in cls.genres[:-1]:
            pass 

    @classmethod
    def add_to_artists(cls):
        if cls.artists[-1] not in cls.artists[:-1]:
            pass 

    @classmethod
    def add_to_genre_count(cls):
        genre = cls.genres[-1]
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls):
        artist = cls.artists[-1]
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


