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
           ("distance", "class")
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
           >>> np.isclose(distance_and_class.column(0).item(1), 0.0104617)
           True
           >>> distance_and_class.column(1).item(1)
           "vertical straight-line"
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
