test = {
  'name': 'Question 1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(extra_info) == list
          True
          >>> type(extra_info[0]) == int # Please format your answer as a list of integers.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sorted(extra_info) == [1, 3]
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
