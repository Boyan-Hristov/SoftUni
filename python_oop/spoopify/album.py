from spoopify.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):

        if song in self.songs:
            return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):

        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album"

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

        # for current_song in self.songs:
        #     if current_song.name == song_name:
        #         self.songs.remove(current_song)
        #         return f"Removed song {song_name} from album {self.name}."
        #
        # else:
        #     return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f"Album {self.name}"]
        info.extend([f"== {song.get_info()}" for song in self.songs])
        info.append("")

        return "\n".join(info)


