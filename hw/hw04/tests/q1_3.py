test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> character_count("The quick(!) brown fox jumped over the lazy(?) dog.") is not None # It looks like you forgot to write "return" somewhere.
          True
          >>> character_count("The quick(!) brown fox jumped over the lazy(?) dog.")
          40
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> character_count("The interrobang ?! is my favorite punctuation mark.")
          41
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
