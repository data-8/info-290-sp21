test = {
  'name': 'Question 2.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != 3 # Don't count cases where the number stays the same as either an increase or a decrease.
          True
          >>> two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != 1 # Don't count cases where the number stays the same as either an increase or a decrease.
          True
          >>> two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != -2 # You might have flipped the difference.
          True
          >>> two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11))
          2
          >>> two_year_changes(ak.column('Murder rate in Alaska'))
          -5
          >>> two_year_changes(mn.column('Murder rate in Minnesota'))
          6
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
