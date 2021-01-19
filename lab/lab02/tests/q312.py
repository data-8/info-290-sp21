test = {
  'name': 'Question 3.1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import IPython.display
          >>> type(art) == IPython.core.display.Image # It looks like you didn't load an image.  Hint: your code should start like this: art = IPython.display.Image(...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 'The_Death_of_Socrates' in art.url # It looks like you loaded the wrong image.
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
