test = {
  'name': 'Question 3_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(celsius_max_temperatures) != 356705.0 # It looks like you multiplied and subtracted in the wrong order
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(celsius_max_temperatures)
          1280677.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(celsius_max_temperatures)
          65000
          >>> celsius_max_temperatures.item(2003)
          20.0
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