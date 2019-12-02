import unittest
import unittest.mock
import gen

class UnitTests(unittest.TestCase):

  def test_get_lyrics_for_artist(self):
    def fake_get_titles_for_artist(artist, max_songs):
      return ['Hold Up', 'Run the World']

    def fake_get_lyrics_for_song(title, artist):
      fakes = {
        'Run the World': ['boy', 'you', 'know', 'you', 'love', 'it'],
        'Hold Up': ['they', 'don\'t', 'love', 'you', 'like', 'I', 'love', 'you']
      }
      return fakes.get(title)

    with unittest.mock.patch('itunes.get_titles_for_artist') as fake_titles:
      with unittest.mock.patch('itunes.get_lyrics_for_song') as fake_lyrics:
        fake_titles.side_effect = fake_get_titles_for_artist
        fake_lyrics.side_effect = fake_get_lyrics_for_song
        lyrics_for_artist = gen.get_lyrics_for_artist('Beyonce', 75)
        fake_titles.assert_called_with('Beyonce', 75)
        fake_lyrics.assert_any_call('Run the World', 'Beyonce')
        fake_lyrics.assert_any_call('Hold Up', 'Beyonce')
        self.assertEqual(lyrics_for_artist, {
          'Run the World': ['boy', 'you', 'know', 'you', 'love', 'it'],
          'Hold Up': ['they', 'don\'t', 'love', 'you', 'like', 'I', 'love', 'you']
      })

  def test_get_bigrams_for_song(self):
    self.assertEqual(gen.get_bigrams_for_song(['boy', 'you', 'know', 'you', 'love', 'it']), {
      'boy': ['you'],
      'you': ['know', 'love'],
      'know': ['you'],
      'love': ['it'],
    })
  
  def test_get_bigrams_for_artist(self):

    lyrics_for_artist = {
      'Run the World': ['boy', 'you', 'know', 'you', 'love', 'it'],
      'Hold Up': ['they', 'don\'t', 'love', 'you', 'like', 'I', 'love', 'you']
    }


    bigrams_for_artist = gen.get_bigrams_for_artist(lyrics_for_artist)
    self.assertEqual(bigrams_for_artist, {
      'boy': ['you'],
      'you': ['know', 'love', 'like'],
      'know': ['you'],
      'love': ['it', 'you', 'you'],
      'they': ['don\'t'],
      'don\'t': ['love'],
      'like': ['I'],
      'I': ['love']
    })


def run_tests():
  print('>>>>>>>>>> RUNNING TESTS <<<<<<<<<<')
  suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
  unittest.TextTestRunner().run(suite)