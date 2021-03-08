test = {
  'name': 'Question 3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 <=  approximate_probability_of_false  <= 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> approximate_probability_of_false > 0.1 # "If you're failing the test, try running the cell again! If that doesn't fix it, then something is wrong with your code."
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
