test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(simulate_several_key_strikes(15))
          15
          >>> isinstance(simulate_several_key_strikes(15), str) # Make sure your function returns a string.
          True
          >>> import numpy as np
          >>> 26 >= len(np.unique(list(simulate_several_key_strikes(500)))) >= 20 # It looks like your simulation doesn't use all the letters, or it uses more than the 26 lower-case letters.
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
