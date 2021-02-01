test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> "(No previous year)" not in with_previous_compensation.column("% Change") # Make sure to remove the "(No previous year)" CEOs
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import math
          >>> t = with_previous_compensation.sort("2014 Total Pay ($)", descending = True)
          >>> value = t.column("2014 Total Pay ($)").item(0)
          >>> math.isclose(value, 67700000.0, rel_tol = 1000) # You have the column, but some of your values may be wrong
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> with_previous_compensation.num_rows == 81 # You have the column, but your number of rows is off
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
