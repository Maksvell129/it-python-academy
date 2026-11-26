class Playlist:
    def __init__(self, tracks, banned_tracks):
        self.tracks = list(tracks)
        self.banned_tracks = list(banned_tracks)

    def __iter__(self):
        for track in self.tracks:
            if track not in self.banned_tracks:
                yield track


tracks = ["lala", "L<<>", "lala2", "olala"]
banned = ["L<<>", "olala"]

playlist = Playlist(tracks, banned)


gen = iter(playlist)

for track in gen:
    print(track)


for track in gen:
    print(track)