test = {
  'name': 'Question 2_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> greatest_nei.take(0)
          Date       | NEI     | NEI-PTER
          2009-10-01 | 10.9698 | 12.8557
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> greatest_nei.num_rows
          10
          >>> np.isclose((sum(greatest_nei.column("NEI"))), 106.61859999999999)
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
