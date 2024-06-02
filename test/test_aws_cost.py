import unittest
from cloud_cost_comparator import get_aws_cost

class TestAWSCost(unittest.TestCase):
    def test_get_aws_cost(self):
        cost = get_aws_cost('t2.micro', 'us-east-1', 100)
        self.assertIsNotNone(cost)
        self.assertGreater(cost, 0)

if __name__ == '__main__':
    unittest.main()
