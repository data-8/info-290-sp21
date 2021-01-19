test = {
  'name': 'Question 2.2.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> start in (-753, -752) # Try assigning start to a negative integer based on founded. For example: start = int(founded.replace('BC ', '-'))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end in (409, 410) # Try assigning end to a positive integer based on sacked. You can replace some part of a string with nothing. For example: end = int(sacked.replace('AD ', ''))
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> end-start in (1163, 1162)
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
