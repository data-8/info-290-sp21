test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> -1 <= r <= 1 # Correlation is a number between -1 and 1
          True
          >>> std_units(np.arange(5)) is None or np.allclose(std_units(np.arange(5)), [-1.41421356, -0.70710678,  0,  0.70710678,  1.41421356]) #It appears that you implemented std_units, but did so incorrectly
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(r, 0.925032576418278)
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
