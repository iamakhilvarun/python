class Song:
    """Class to represent a song
        Attributes:
            title (str): The title of the song
            artist (Artist): An Artist object representing the song creator.
            duration (int) : The duration of the song in seconds . May be zero
        """

    def __init__(self,title,artist,duration=0):
        """Song init method
        Args:
         title (str): Intializes the 'title' attribute
         artist (Artist) : At artist object represeting the song's creator.
         duration (optional [int]) : intial value for the 'duration' attribute.
                    will default to zero if not specified
        """
        self.title=title
        self.artist=artist
        self.duration=duration