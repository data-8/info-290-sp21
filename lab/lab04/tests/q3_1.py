test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(some_functions)
          3

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> callable(some_functions.item(0)) # The first thing in your array may not be a function
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> callable(some_functions.item(1)) # The second thing in your array may not be a function
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> callable(some_functions.item(2)) # The third thing in your array may not be a function
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
