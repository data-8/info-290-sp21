test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(mark_hurd_pay) != str # Your answer should be a number
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mark_hurd_pay != 5325 # Don't forget to give your answer in dollars, not millions of dollars!
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mark_hurd_pay == 53250000 # Don't forget to give your answer in dollars, not millions of dollars!
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
