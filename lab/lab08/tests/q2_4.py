test = {
  'name': 'Question 2.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> num_changes != 50 # There are several two-year changes for each state.
          True
          >>> not(42 <= num_changes <= 44) # The entire data set contains many states, not just 1.
          True
          >>> 2000 <= num_changes <= 2200
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> num_changes == 2100
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
