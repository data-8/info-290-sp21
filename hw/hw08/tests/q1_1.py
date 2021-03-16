test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(proportions_in_resamples()) == 5000 # You're not creating 5000 resamples
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> 0.4 < np.mean(proportions_in_resamples()) < 0.55
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(proportions_in_resamples() == 0.47)
          False
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
