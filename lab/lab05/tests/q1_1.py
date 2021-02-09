test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(b_pop) == type(...) # Looks like you haven't started yet
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> b_pop.labels == ('time', 'population_total') # Check your column labels and spelling
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(b_pop.sort("time").column("time") == np.arange(1970, 2016)) # Times should range from 1970 through 2015
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> b_pop.sort("time", descending=True).column("population_total").item(0) # See if you selected the right three-letter code!
          160995642
          >>> b_pop.sort("time").column("population_total").item(0)
          65048701
          """,
          'hidden': True,
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
