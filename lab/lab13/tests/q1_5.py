test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> abs(fit_line(example_table)[0] - 2) < .5 # Testing the slope
          True
          >>> abs(fit_line(example_table)[1] - 1) < .5 # Testing the intercept
          True
          >>> abs(fit_line(close_novas)[0] - 14094) < 5 # Testing the slope
          True
          >>> abs(fit_line(close_novas)[1] - 2) < .5 # Testing the intercept
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
