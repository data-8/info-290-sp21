test = {
  'name': 'Question 1.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ca_change > 0 # You might have flipped the difference.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(np.round(ca_change), 726) # You might have flipped the difference.
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
