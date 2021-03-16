test = {
  'name': 'q1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> mean_based_estimator(np.array([1, 2, 3])) is not None # It looks like you forgot to return something.
          True
          >>> int(np.round(mean_based_estimator(np.array([1, 2, 3])))) # It looks like your function doesn't compute the right estimate.  For consistency in the rest of the lab, it's best if you use the twice-the-mean estimate, even if you prefer some other estimate.
          4
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
