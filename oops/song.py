class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds.  May be zero
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]: Initial value for the 'duration' attribute.
                Will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent an album, using it's track list

    Attributes:
        name(str): The name of the album
        year(int) : Year the album released
        artist(str) : The artist responsible for the album.
        If not specified, the artist will default to an artist with name "various artists"
        tracks(List[Song]) : A list of Song on album

    Methods:
        addSong: Used to add song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("various artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the track list
        Args:
            song(Song): A song  to add.
            position(original[int]): If specified, the song will be added to that position
                in the track list- inserting it between other song if necessary.
                Otherwise the song will be added to the end of list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    Attributes:
        name(str): The name of the artist
        albums(List[Album]: A list of the albums by the artist.
            The list includes only those album in this collection, it is not an
            exhaustive list of the artist's published albums.

        Methods:
            add_album: Use to add new album to the artist album list.
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album(Album): Album object to add to list.
                If the album is already present, it will not be added again(although this is yet to be implemented)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            # data raw consist of Tuple-> (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We have just read details of new artist
                # Store the current album in the current artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

            # After reading the last line of the text file, we will have an artist and album that haven't been store-
            # process them now.
            if new_artist is not None:
                if new_album is not None:
                    new_artist.add_album(new_album)
                artist_list.append(new_artist)

    return artist_list


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists".format(len(artists)))

# help(Song)
# print(Song.__doc__)
# print(Song.__init__.__doc__)