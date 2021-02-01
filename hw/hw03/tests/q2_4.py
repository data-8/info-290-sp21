test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(pter)
          90
          >>> round(pter.item(6), 4) != -1.1282 # It looks like you subtracted in the wrong order.
          True
          >>> round(pter.item(6), 4)
          1.1282
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(sum(pter))
          107.0
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
