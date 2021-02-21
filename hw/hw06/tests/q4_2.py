test = {
  'name': 'Question 4_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> representative_sample.num_rows == 500 # The sample should be of size 500.
          True
          >>> all(np.in1d(representative_sample.column('mag'), earthquakes.column('mag'))) # Your sample should have the same columns as the original table, and all data in the sample should be present in the original table.
          True
          >>> representative_mean < max(representative_sample.column('mag')) and representative_mean > min(representative_sample.column('mag')) # The mean can't be bigger than the biggest magnitude, or smaller than the smallest!
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 4.7 < representative_mean < 4.9
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
