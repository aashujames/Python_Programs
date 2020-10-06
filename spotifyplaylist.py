playlist = {
    'title': 'morning mood',
    'author': 'ashish',
    'songs': [
        {'title': 'boyfriend', 'artist': ['jb'], 'duration': 3.5},
        {'title': 'love me', 'artist': ['larry', 'kane'], 'duration': 5.0},
        {'title': 'bailando', 'artist': ['enrique'], 'duration': 4.25},
    ]
}

total_length=0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)