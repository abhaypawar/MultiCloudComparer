import unittest
from cloud_cost_comparator import get_azure_cost

class TestAzureCost(unittest.TestCase):
    def test_get_azure_cost(self):
        cost = get_azure_cost('Standard_B1s', 'eastus', 100)
        self.assertIsNotNone(cost)
        self.assertGreater(cost, 0)

if __name__ == '__main__':
    unittest.main()
