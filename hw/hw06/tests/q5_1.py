test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(coin_model_probabilities) == 2 # The array should have length 2
          True
          >>> sum(coin_model_probabilities) == 1 # The elements in the array should add up to 1.
          True
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> coin_model_probabilities[1]
          0.5
          >>> coin_model_probabilities[0]
          0.5
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
