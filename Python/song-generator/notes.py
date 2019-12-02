# Use **kwargs to unpackage dicts
dict1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
dict2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}

dict3 = {**dict1, **dict2}
print(dict3)

# Use union operator
print(dict(dict1 .items() | dict2.items()))

# Brute force
bigram_for_songs = [
    {'Ritika': 5, 'Sam': [1, 2, 3], 'John': 10},
    {'Aadi': 8, 'Sam': [4, 5, 6], 'Mark': 11},
    {'idk': 3, 'hi': 24, 'temp': 123}
]

result = {}

for bigram in bigram_for_songs:
    for i, v in bigram.items():
        if i not in result:
            result[i] = v
        else:
            result[i] = result[i] + v

print(result)

#######
lyrics_for_artist = {
    'Halo': ['Rember', 'those', 'etc'],
    'Single lady': ['hi', 'hello', 'etc'],
}

bigram_for_songs = []
for _i, v in lyrics_for_artist.items():
    bigram_for_songs.append(get_bigrams_for_song(v))

#######
random_lyrics = ''
word = random.choice(list(bigrams_for_artist.keys()))

for i in range(num_words):
    random_lyrics += word
    word = random.choice(bigrams_for_artist[word])
