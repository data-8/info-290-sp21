test = {
  'name': '2.3.1.',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Fill in the row
          >>> #   time = ...
          >>> # with something like:
          >>> #   time = 4.567
          >>> # (except with the right number).
          >>> time != ... # Fill in the row: time = ... with something like: time = 4.567 (except with the right number).
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(time, 5) # Read the text above the question to see what time should be.
          1.2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> estimated_distance_m != ... # Fill in the row: estimated_distance_m = ... with something like: estimated_distance_m = 4.567 (except with the right number).
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> estimated_distance_m != 113 # Note that the units are meters, but the text used centimeters.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(estimated_distance_m, 5) # Read the text above to see what estimated_distance_m should be.
          1.13
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
