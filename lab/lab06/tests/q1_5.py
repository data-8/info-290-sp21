test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 2 < number_wow_reactions < 6
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> number_wow_reactions == 4 # Incorrect value for number_wow_reactions
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
