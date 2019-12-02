import requests
import json
import random
import itunes
from itunes import get_titles_for_artist
from itunes import get_lyrics_for_song

## CODE Here ##


def get_lyrics_for_artist(artist, max_songs):
  """Creates a dictionary of song title to lyrics.

  Args:
    artist: The artist to look up songs for.
    max_songs: The maximum number of songs to look up.

  Returns:
    A dictionary of lyrics for the given artist,
    where the keys are song titles and the values
    are the lyrics for the song as a list of words.
  """


song = {}
title = 0
singer = itunes.get_titles_for_artist(artist, max_songs)
 for i in range(len(singer)):
    title = singer[i]
    lyrics = itunes.get_lyrics_for_song(title, artist)
    song[title] = lyrics
  return song


def get_bigrams_for_song(lyrics):
  """Creates a dictionary of bigrams in a single song.

  Args:
    lyrics: A list of the words in a song's lyrics.

  Returns:
    A dictionary of lyric bigrams, where the keys are
    words and the values are a list of all the words
    that directly follow that word in the lyrics.
  """
  bigrams = {}
  for i in range(len(lyrics)-1):
    if lyrics[i] not in bigrams:
      bigrams[lyrics[i]] = []
      # makes sure all keys are unique
    bigrams[lyrics[i]].append(lyrics[i+1])
  return bigrams


def get_bigrams_for_artist(lyrics_for_artist):
  """Creates a dictionary of bigrams for an artist.
  
  Args:
    lyrics_for_artist: A dictionary of song title to lyrics.
  
  Returns:
    A single dictionary of lyric bigrams for all of the
    artist's songs, where the keys are words and the
    values are a list of all the words that directly
    follow that word in the lyrics.
  """
  # get_bigrams_for_artist({'Run the World': ['boy', 'you', 'know', 'you', 'love', 'it'],'Hold Up': ['they', 'don\'t', 'love', 'you', 'like', 'I', 'love', 'you']})
  ###
  song_bigrams = {}
  for song in get_bigrams_for_artist:
    lyrics = get_bigrams_for_artist[song]
    bigram = get_bigrams_for_song(lyrics)
    song_bigrams.append(bigram)
  return song_bigrams


def make_song(bigrams_for_artist, num_words):
  """Generates a song based on common bigrams.
  
  Args:
    bigrams_for_artist: A dictionary of bigrams for an artist.
    num_words: The number of words in the generated song.
  
  Returns:
    Randomly generated lyrics using the bigrams found in the
    artist's body of work.
  """
  pass


---------------

File Name: itunes.py

###################################
# DO NOT MODIFY THIS FILE
###################################


def get_titles_for_artist(artist, max_songs):
  """Fetches a list of tracks for the given artist.
  
  Args:
    artist: The artist name.
    max_songs: The maximum number of songs to fetch.
  
  Returns:
    A list of song titles for the given artist,
    as retrieved from the iTunes Search API.
  """
  url = 'https://itunes.apple.com/search?entity=song&limit=' + \
      str(max_songs) + '&term=' + artist.lower()
  response = requests.get(url)

  if response.status_code != 200:
    # Could not find any songs for the given artist.
    print('ERROR: artist "' + artist + '" not found.')
    return []

  results = json.loads(response.text)['results']

  # Collect all the song titles from the API response.
  tracks = []
  for track in results:
    title = track['trackName']

    if ' (feat.' in title:
      # Remove the artist feature from the
      # song title (e.g. change
      # 'We Are (feat. Nas)' to 'We Are').
      title = title[:title.index(' (feat.')]

    tracks.append(title)

  return list(set(tracks))


def get_lyrics_for_song(title, artist):
  """Fetches the lyrics for the given song.
  
  Args:
    title: The song title. Spelling and case sensitive.
    artist: The artist name. Spelling and case sensitive.

  Returns:
    A list of the words in the lyrics for the given
    song, in order,  as retrieved from the lyrics.ovh
    API.
  """
  url = 'https://api.lyrics.ovh/v1/' + artist + '/' + title
  response = requests.get(url)

  if response.status_code != 200:
    # Could not find the lyrics for the given
    # song and artist.
    print('...lyrics for "' + title + '" not found')
    return []

  # Convert all the lyrics to lowercase for
  # consistency and split the lyrics into a
  # list of words.
  lyrics = json.loads(response.text)['lyrics']
  return lyrics.lower().split()
