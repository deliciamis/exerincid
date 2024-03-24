def test():
  """Tests the `test` function."""

  # Create a new test case.
  test_case = unittest.TestCase()

  # Assert that the `test` function returns the correct value.
  test_case.assertEqual(test(), 'Hello, world!')
