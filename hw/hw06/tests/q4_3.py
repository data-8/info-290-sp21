test = {
  'name': 'Question 4_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(maximums) != 0 # It looks like your maximums array is empty!
          True
          >>> len(maximums) == 5000
          True
          >>> max(maximums) <= max(earthquakes.column('mag')) # The biggest simulated maximum can't be bigger than the actual maximum!
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
