import datetime

class Song:
    def __init__(self, title, artist, album, leng):
        self.title = title
        self.artist = artist
        self.album = album
        self.len = leng
        self.length_in_seconds = __length_string_to_sec(self.leng)

    def __length_string_to_sec(length_str):
        arr = length_str.split(":")
        print(arr[0])
        song_len = 0
        time_coeff = 1
        for i in range(len(arr)-1, -1, -1):
            print("i", i)
            song_len += int(arr[i]) * time_coeff
            time_coeff *= 60
        return song_len

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.title, self.artist, self.album, self.length)

    def __eq__(self, other):
        return self.title==other.title and self.artist==other.artist and self.album==other.album and self.length==other.length

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return self.length_in_seconds
        if minutes:
            return self.length_in_seconds // 60
        if hours:
            return self.length_in_seconds // 3600
        return self.leng

