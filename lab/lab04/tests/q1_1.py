test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy
          >>> total_pay_type != numpy.ndarray # Make sure you are examining the values in the column, not the column itself
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'str' in str(total_pay_type)
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> total_pay_type != int # Make sure to call the type function on a value in the column
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
