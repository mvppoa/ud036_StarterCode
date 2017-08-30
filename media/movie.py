import webbrowser

from media.video import Video


class Movie(Video):
    """This is a class containing movies"""

    def __init__(self, title, duration, classification,
                 storyline, poster_image_url, trailer_youtube_url):
        super().__init__(title, duration, classification)
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Method to open youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)
