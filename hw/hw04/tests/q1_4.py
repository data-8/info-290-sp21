test = {
  'name': 'Question 1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> chapter_number("XIV. Chapter Fourteen\nIt was the most mediocre of times...") is not None # It looks like you forgot to write "return" somewhere.
          True
          >>> chapter_number("XIV. Chapter Fourteen\nIt was the most mediocre of times...")
          'XIV'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> chapter_number("I. Chapter One\nIt was the best of times, it was...")
          'I'
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
