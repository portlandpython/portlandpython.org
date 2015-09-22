from django.test import TestCase


class SampleDjangoTests(TestCase):

    def test_travis_setup(self):
        """
        This test method is simply for the purpose of showing
        a travis CI setup.
        The test file needs to be refactored into a better folder structure.
        """
        result = 1 + 1
        self.assertEqual(result, 2)
