test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(resampled_means) == type(make_array())
          True
          >>> len(resampled_means) == 5000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> all(x == resampled_means[0] for x in resampled_means)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 88 < (sum(resampled_means) / 5000) < 95
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
