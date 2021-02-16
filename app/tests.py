from django.test import TestCase

# Create your tests here.

class TestCI(TestCase):
  def test_continuous_integration(self):
    self.assertEqual(2 + 2, 4)
