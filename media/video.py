class Video:

    """Core class of the media file. Can be inherited by other classes """

    def __init__(self, title, duration, classification):
        self.title = title
        self.duration = duration
        self.classification = classification
