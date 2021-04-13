test = {
  'name': 'Question 2_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> total_squared_error(0, 0) is not None # It looks like you forgot to return something.
          True
          >>> np.isclose(15.25**0.5, total_squared_error(0, 0)) # It looks like you took a square root, but we didn't want you to do that in this exercise.
          False
          >>> np.isclose(15.25, total_squared_error(0, 0)) # Your calculation is incorrect in some way.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>>
          >>> total_squared_error(5, 10)
          2350.25
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
