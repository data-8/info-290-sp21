test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simulate_key_strike() is not None # It looks like you forgot to have your function return something.
          True
          >>> import string
          >>> all([simulate_key_strike() in string.ascii_lowercase for i in range(100)])
          True
          >>> import numpy as np
          >>> 26 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 20 # It looks like you didn't use all the letters of the alphabet, or you used too many.
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
