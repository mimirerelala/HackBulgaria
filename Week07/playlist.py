import tabulate
import song
import random

class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__list_songs = []

    def add_song(self, song):
        if song not in self.__list_songs:
            self.__list_songs.append(song)
        else:
            raise SongAlreadyInPlaylistError("Cannot add it again!")

    def remove_song(self, song):
        if song in self.__list_songs:
            self.__list_songs.remove(song)
        else:
            raise SongNotInPlaylistError("Cannot remove a song if it is not in the playlist")

    def add_songs(self, songs):
        for song in songs:
            self.__list_songs.append(song)

    def total_length(self):
        total_time = 0
        for song in self.__list_songs:
            total_time += song.length_in_seconds
        return total_time

    def artists(self):
        artists_dict = {}
        for song in self.__list_songs:
            if song.artist not in artists_dict:
                artists_dict[song.artist] = 1
            else:
                artists_dict[song.artist] += 1

    def next_song(self):
        if self.shuffle:
            return self.__list_songs[random.randint(0, len(self.__list_songs))]
        
        pass

    def pprint_playlist(self):
        pass

    def save(self):
        pass

    @staticmethod
    def load(path):
        pass


class SongAlreadyInPlaylistError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class SongNotInPlaylistError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)