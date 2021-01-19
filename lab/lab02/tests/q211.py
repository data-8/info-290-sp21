test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(you) == str # To understand how this question works, first set: you = 'fi' and add the line: print('beeper'.replace('p', you)) and you should see the word "beefier" appear as the first output. Also, just by changing you, you can create a word with two double letters in a row: beekeeper
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'beeper'.replace('p', you)[::-1] # You can make the word beekeeper by assigning: you = 'keep'
          'repeekeeb'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'beeper'.replace('p', you).replace('bee', this)[::-1] # The word you're trying to make is "bookkeeper"! To change "beekeeper" to "bookkeeper", change the "bee" to "book".
          'repeekkoob'
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
