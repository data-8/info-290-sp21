test = {
  'name': 'Question 1_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
           >>> len(train_distances)
           660
           >>> distance_and_class.labels
           ('distance', 'class')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
           >>> np.isclose(distance_and_class.column(0).item(0), 0.21429737091034312)
           True
           >>> distance_and_class.column(1).item(0) == 'vertical straight-line'
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
