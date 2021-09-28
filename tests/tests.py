import unittest
from activity import eat, nap

class ActivityTests(unittest.TestCase):
  def setUp(self):
      """Start your engines!!!"""
      self.assertEqual(True, True)
  def test_eat_healthy(self):
    """Testing Eat Healthy, health & wealth & that ish"""
    self.assertEqual(eat("kagel", is_healthy=True),
                      "I dey chow kagel, whatever it means. Rubber maybe?"
                    )

  def test_eat_unhealthy(self):
    """Testing Eat UnHealthy, cheat days"""
    self.assertEqual(eat("pizza", is_healthy=False),
                      "I dey chow pizza, if I perish I perish!"
                    )

  def tearDown(self):
      """Stoping engines!!"""

if __name__ == "__main__":
  unittest.main()