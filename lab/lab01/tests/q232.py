test = {
  'name': '2.3.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> predicted_distance_m != ... # Fill in the line that currently says: predicted_distance_m = ... in the cell above.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(predicted_distance_m, 5) # Compute predicted_distance_m using the formula in the text above. Hint: it should start with something like this: predicted_distance_m = (1/2) * gravity_constant ...
          1.17022
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(difference, 5)
          0.04022
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
