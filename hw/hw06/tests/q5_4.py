test = {
  'name': 'Question 5_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(coin_statistics) == repetitions # There should be exactly as many elements in coin_statistics as the number 'repetitions'
          True
          >>> all([0 <= k <= 10 for k in coin_statistics]) # Each element of coin_statistics should be between 0 and 10 inclusive
          True
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
