test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'word_count' in globals() # It looks like you haven't defined a function named word_count.
          True
          >>> callable(word_count) # It looks like you haven't defined a function named word_count.
          True
          >>> word_count("The quick brown fox") is not None # It looks like you forgot to write "return" somewhere.
          True
          >>> word_count("The quick brown fox")
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> word_count(tale_chapters.column("Chapter text").item(0))
          911
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
