import unittest
from cloud_cost_comparator import get_gcp_cost

class TestGCPCost(unittest.TestCase):
    def test_get_gcp_cost(self):
        cost = get_gcp_cost('n1-standard-1', 'us-central1', 100)
        self.assertIsNotNone(cost)
        self.assertGreater(cost, 0)

if __name__ == '__main__':
    unittest.main()
