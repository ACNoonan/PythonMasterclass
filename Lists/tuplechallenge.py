# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Tom Waltz"))

# Challenge: Write code to print the album details, followed by
# a listing of all the tracks in the album.

# Indent the tracks by a single tab when print them.
# Answer to Original Challenge:
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title: {}".format(track, title))

imelda = "More Mayhem", "Imelda May", 2011, (
     [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Tom Waltz")])
print(imelda)

# Appending (changing) a mutable list within an immutalbe tuple
title, artist, year, tracks = imelda
tracks.append((6, 'Eternity'))

print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print('\tTrack number {}, Title: {}'.format(track, title))