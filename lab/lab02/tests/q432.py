test = {
  'name': 'Question 4.3.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> type(total_charges) == np.ndarray # It looks like you're not making an array.  You shouldn't need to use .item anywhere in your solution.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> sum(abs(total_charges - np.array([24.144, 47.88, 37.212]))) < 1e-6 # You made an array, but it doesn't have the right numbers in it.
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
