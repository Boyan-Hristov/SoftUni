from spoopify.album import Album
from spoopify.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, current_album: Album):
        if current_album in self.albums:
            return f"Band {self.name} already has {current_album.name} in their library."

        self.albums.append(current_album)
        return f"Band {self.name} has added their newest album {current_album.name}."

    def remove_album(self, album_name: str):

        try:
            current_album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if current_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(current_album)
        return f"Album {album_name} has been removed."

        # for current_album in self.albums:
        #     if current_album.name == album_name:
        #
        #         if current_album.published:
        #             return "Album has been published. It cannot be removed."
        #
        #         self.albums.remove(current_album)
        #         return f"Album {album_name} has been removed."
        #
        # else:
        #     return f"Album {album_name} is not found."

    def details(self):
        info = [f"Band {self.name}"]
        info.extend([current_album.details() for current_album in self.albums])

        return "\n".join(info)


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

