test = {
  'name': 'q3_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> new_left_end < 150 < new_right_end # If you're failing this test, try to re-run the cell and see if you pass it
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> new_observations.num_rows
          17
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(new_bootstrap_estimates) == 5000
          True
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
