test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 40 <= shortest <= 50 # Hint: shortest is a number between 40 and 50.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 70 <= longest <= 130 # Hint: longest is a number between 70 and 130.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shortest <= average <= longest # Hint: the average is between the shortest and the longest
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> shortest
          43
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> longest
          96
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.round(average, 2)
          70.9
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
