test = {
  'name': 'q3_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(bootstrap_estimates)
          5000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 110 < np.mean(bootstrap_estimates) < 130
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
