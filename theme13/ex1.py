class _PlaylistIterator:
    def __init__(self, tracks, banned_tracks):
        self.tracks = tracks
        self.banned_tracks = banned_tracks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):



        while self.index < len(self.tracks):
            track = self.tracks[self.index]
            self.index += 1

            if track not in self.banned_tracks:
                return track

        raise StopIteration


class Playlist:
    def __init__(self, tracks, banned_tracks):
        self.tracks = list(tracks)
        self.banned_tracks = list(banned_tracks)

    def __iter__(self):
        return _PlaylistIterator(self.tracks, self.banned_tracks)

tracks = ["lala", "L<<>", "lala2", "olala"]
banned = ["L<<>", "olala"]

playlist = Playlist(tracks, banned)

for track in playlist:
    print(track)