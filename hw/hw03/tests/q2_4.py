test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(pter)
          90
          >>> round(pter.item(6), 4) != -1.1282 # It looks like you subtracted in the wrong order.
          True
          >>> round(pter.item(6), 4)
          1.1282
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(sum(pter), 107.31349999999999)
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
