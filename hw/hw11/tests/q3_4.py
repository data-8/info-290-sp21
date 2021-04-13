test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(resample_slopes) == 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(resample_slopes == resample_slopes[0]) # Make sure you're randomly sampling
          False
          """,
          'hidden': False,
          'locked': False
        }
        {
          'code': r"""
          >>> import numpy as np
          >>> 9 < np.mean(resample_slopes) < 12
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
