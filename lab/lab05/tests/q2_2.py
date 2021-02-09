test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pop_by_decade.labels == ('decade', 'population') # Check your column labels and spelling
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_by_decade.column(0).item(0) == 1960 # The first year of the 1960's is 1960.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> pop_by_decade.num_rows == 6
          True
          >>> pop_by_decade.column(0).item(0) == 1960
          True
          >>> pop_by_decade.column(0).item(5) == 2010
          True
          >>> pop_by_decade.column(1).item(1) == 3211487418
          True
          >>> pop_by_decade.column(1).item(5) == 6040810517
          True
          """,
          'hidden': True,
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
