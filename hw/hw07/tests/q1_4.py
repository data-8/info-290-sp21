test = {
  'name': 'Question 1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.std([simulate() for _ in range(1000)]) > 0 # It looks like your simulation isn't random.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 <= simulate() <= 20
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
