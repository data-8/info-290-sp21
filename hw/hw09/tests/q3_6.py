test = {
  'name': 'Question 3_6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> michelle_sample_size == 9975 # michelle_sample_size should be Michelle's sample size!
          True
          >>> smaller_sample_size < michelle_sample_size # smaller_sample_size should be smaller than Michelle's sample size!
          True
          >>> larger_sample_size > michelle_sample_size # larger_sample_size should be larger than Michelle's sample size!
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(michelle_sample_mean_sd, 0.005000, atol = 0.0001)
          True
          >>> smaller_sample_mean_sd > michelle_sample_mean_sd
          True
          >>> larger_sample_mean_sd < michelle_sample_mean_sd
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
