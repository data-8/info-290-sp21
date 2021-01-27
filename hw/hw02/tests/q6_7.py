test = {
  'name': 'Question 6_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> remaining_inventory.num_columns # It looks like your table doesn't have all 3 columns that are in the inventory table.
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> remaining_inventory.column("count").item(0) != 45 # It looks like you forgot to subtract off the sales.
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> remaining_inventory.where(1, 'grape')
          box ID | fruit name | count
          57930  | grape      | 162
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
